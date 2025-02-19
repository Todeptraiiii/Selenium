----------------------------------------------------------------------------------
-- Company: Lancsnet
-- Engineer: 2
-- 
-- Create Date: 10/06/2023 08:45:38 AM
-- Design Name: 
-- Module Name: uart_wrapper - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity uart_wrapper is
Generic (
    clk_freq    :  INTEGER    := 50_000_000;  --frequency of system clock in Hertz
    baud_rate   :  INTEGER    := 19_200;      --data link baud rate in bits/second
    os_rate     :  INTEGER    := 16;          --oversampling rate to find center of receive bits (in samples per baud period)
    d_width     :  INTEGER    := 8;           --data bus width
    parity      :  INTEGER    := 0;           --0 for no parity, 1 for parity
    parity_eo   :  STD_LOGIC  := '0';         --'0' for even, '1' for odd parity
    numbyte     :  INTEGER    := 1);          --number_of_bytes/utxdata for tx transfer
Port ( 
    clk          : in  STD_LOGIC;
    rst          : in  STD_LOGIC;
    rx           : in  STD_LOGIC;
    tx           : out STD_LOGIC;
    urx_data     : out STD_LOGIC_VECTOR (7 downto 0);
    urx_valid    : out STD_LOGIC;
    utx_clock    : in  STD_LOGIC; -- async tx clk?
    utx_data     : in  STD_LOGIC_VECTOR (numbyte * 8 - 1 downto 0);
    utx_valid    : in  STD_LOGIC;
    utx_ready    : out STD_LOGIC);
end uart_wrapper;

architecture Behavioral of uart_wrapper is

component uart_scott IS
GENERIC(
    clk_freq    :  INTEGER    := 50_000_000;  --frequency of system clock in Hertz
    baud_rate   :  INTEGER    := 19_200;      --data link baud rate in bits/second
    os_rate     :  INTEGER    := 16;          --oversampling rate to find center of receive bits (in samples per baud period)
    d_width     :  INTEGER    := 8;           --data bus width
    parity      :  INTEGER    := 0;           --0 for no parity, 1 for parity
    parity_eo   :  STD_LOGIC  := '0');        --'0' for even, '1' for odd parity
PORT(
    clk         :  IN   STD_LOGIC;                             --system clock
    reset_n     :  IN   STD_LOGIC;                             --ascynchronous reset
    tx_ena      :  IN   STD_LOGIC;                             --initiate transmission
    tx_data     :  IN   STD_LOGIC_VECTOR(d_width-1 DOWNTO 0);  --data to transmit
    rx          :  IN   STD_LOGIC;                             --receive pin
    rx_busy     :  OUT  STD_LOGIC;                             --data reception in progress
    rx_error    :  OUT  STD_LOGIC;                             --start, parity, or stop bit error detected
    rx_data     :  OUT  STD_LOGIC_VECTOR(d_width-1 DOWNTO 0);  --data received
    tx_busy     :  OUT  STD_LOGIC;                             --transmission in progress
    tx          :  OUT  STD_LOGIC				               --transmit pin
);                            
END component;

component axis_async_fifo_adapter is
Generic (
    DEPTH                  : integer := 4096;
    S_DATA_WIDTH           : integer := 8;
    S_KEEP_ENABLE          : integer := 1;
    S_KEEP_WIDTH           : integer := 1;
    M_DATA_WIDTH           : integer := 8;
    M_KEEP_ENABLE          : integer := 1;
    M_KEEP_WIDTH           : integer := 1;
    ID_ENABLE              : integer := 0;
    ID_WIDTH               : integer := 8;
    DEST_ENABLE            : integer := 0;
    DEST_WIDTH             : integer := 8;
    USER_ENABLE            : integer := 1;
    USER_WIDTH             : integer := 1;
    RAM_PIPELINE           : integer := 1;
    OUTPUT_FIFO_ENABLE     : integer := 0;
    FRAME_FIFO             : integer := 0;
    USER_BAD_FRAME_VALUE   : std_logic := '1';
    USER_BAD_FRAME_MASK    : std_logic := '1';
    DROP_OVERSIZE_FRAME    : integer := 0;
    DROP_BAD_FRAME         : integer := 0;
    DROP_WHEN_FULL         : integer := 0
);
Port (
    s_clk               : in    std_logic := '0';
    s_rst               : in    std_logic := '0';
    s_axis_tdata        : in    std_logic_vector (S_DATA_WIDTH - 1 downto 0) ;
    s_axis_tkeep        : in    std_logic_vector (S_KEEP_WIDTH - 1 downto 0) ;
    s_axis_tvalid       : in    std_logic := '0';
    s_axis_tready       : out   std_logic := '0';
    s_axis_tlast        : in    std_logic := '0';
    s_axis_tid          : in    std_logic_vector (ID_WIDTH   - 1 downto 0) ;
    s_axis_tdest        : in    std_logic_vector (DEST_WIDTH - 1 downto 0) ;
    s_axis_tuser        : in    std_logic_vector (USER_WIDTH - 1 downto 0) ;
    
    m_clk               : in    std_logic := '0';
    m_rst               : in    std_logic := '0';
    m_axis_tdata        : out   std_logic_vector (M_DATA_WIDTH - 1 downto 0) ;
    m_axis_tkeep        : out   std_logic_vector (M_KEEP_WIDTH - 1 downto 0) ;
    m_axis_tvalid       : out   std_logic := '0';
    m_axis_tready       : in    std_logic := '0';
    m_axis_tlast        : out   std_logic := '0';
    m_axis_tid          : out   std_logic_vector (ID_WIDTH   - 1 downto 0) ;
    m_axis_tdest        : out   std_logic_vector (DEST_WIDTH - 1 downto 0) ;
    m_axis_tuser        : out   std_logic_vector (USER_WIDTH - 1 downto 0) ;
    
    s_status_overflow   : out   std_logic := '0';
    s_status_bad_frame  : out   std_logic := '0';
    s_status_good_frame : out   std_logic := '0';
    m_status_overflow   : out   std_logic := '0';
    m_status_bad_frame  : out   std_logic := '0';
    m_status_good_frame : out   std_logic := '0');
end component;

component fallthrough_small_fifo
generic (
    FORCE_DISTRIBUTED   : integer := 0;
    WIDTH               : integer := 72;
    MAX_DEPTH_BITS      : integer := 3;
    PROG_FULL_THRESHOLD : integer := 7
);
port (
    din         : in  std_logic_vector(WIDTH-1 downto 0);
    wr_en       : in  std_logic;
    rd_en       : in  std_logic;
    dout        : out std_logic_vector(WIDTH-1 downto 0);
    full        : out std_logic;
    nearly_full : out std_logic;
    prog_full   : out std_logic;
    empty       : out std_logic;
    reset       : in  std_logic;
    clk         : in  std_logic
);
end component;

component convto8 is
Generic	( n	: integer := 4); 
Port ( 
    CLK 		: in  STD_LOGIC;
    RST 		: in  STD_LOGIC;
    valid	 	: in  STD_LOGIC;
    data 		: in  STD_LOGIC_VECTOR (n*8 - 1 downto 0);
    ready 		: out  STD_LOGIC;
    valid8 	    : out  STD_LOGIC;
    data8 		: out  STD_LOGIC_VECTOR (7 downto 0));
end component;

signal rstn : std_logic := '1';

-- UART
constant FORCE_DISTRIBUTED   : integer := 0;
constant DATA_WIDTH          : integer := 8;
constant MAX_DEPTH_BITS      : integer := 11; 
constant PROG_FULL_THRESHOLD : integer := 2**11-2;

signal tx_ena       : std_logic := '0';
signal tx_data      : std_logic_vector(7 downto 0) := (others => '0');
signal rx_busy      : std_logic := '0';
signal rx_busy_d    : std_logic := '0';
signal rx_error     : std_logic := '0';
signal rx_data      : std_logic_vector(7 downto 0) := (others => '0');
signal tx_busy      : std_logic := '0';
signal tx_busy_d    : std_logic := '0';
signal fifo_empty   : std_logic := '0';
signal fifo_full    : std_logic := '0';
signal urx_tdata    : std_logic_vector (7 downto 0) := (others => '0');   
signal urx_tvalid   : std_logic := '0';    
signal fifo_rd_en   : std_logic := '0';
signal fifo_rd_data : std_logic_vector (7 downto 0) := (others => '0');
signal fifo_wr_en   : std_logic := '0';
signal fifo_wr_data : std_logic_vector (7 downto 0) := (others => '0');
signal fifo_ready   : std_logic := '0';
signal conv8ready   : std_logic := '0'; 

signal swaputx_data : std_logic_vector (numbyte * 8 - 1 downto 0) := (others => '0');
function swap(blk : std_logic_vector) return std_logic_vector is
    variable ret : std_logic_vector(blk'range);
begin
    for i in 0 to ret'length/8-1 loop
        ret(i*8+7 downto i*8) := blk((ret'length/8-1-i)*8+7 downto (ret'length/8-1-i)*8);
    end loop;
    return ret;
end function;
    
begin

rstn        <= not rst;
urx_data    <= urx_tdata;
urx_valid   <= urx_tvalid;

UART_if_inst0: uart_scott
generic map(
    clk_freq    => clk_freq   ,  
    baud_rate   => baud_rate  ,
    os_rate     => os_rate    ,
    d_width     => d_width    ,
    parity      => parity     ,
    parity_eo   => parity_eo
    )  
port map(
    clk         => clk   ,
    reset_n     => rstn  ,
    tx_ena      => tx_ena    ,
    tx_data     => tx_data   ,
    rx          => RX        ,
    rx_busy     => rx_busy   ,
    rx_error    => rx_error  ,
    rx_data     => rx_data   ,
    tx_busy     => tx_busy   ,
    tx          => TX      
    );         
                       
-- RX interface
delay_rx_busy_pr: process(clk)
begin
    if rising_edge(clk) then
        rx_busy_d <= rx_busy;
    end if;
end process delay_rx_busy_pr;

URX_TVALID_pr: process(clk)
begin
    if rising_edge(clk) then
        if rst = '1' then
            URX_TVALID <= '0';
        else
            if rx_busy_d = '1' and rx_busy = '0' then
                URX_TVALID <= '1';
            else
                URX_TVALID <= '0';
            end if;
        end if;
    end if;
end process URX_TVALID_pr;
URX_TDATA <= rx_data;

-- TX interface
swaputx_data <= swap(utx_data);
convert_utx_data_inst1: axis_async_fifo_adapter
    Generic map (
        DEPTH                => numbyte * 4 ,
        S_DATA_WIDTH         => numbyte * 8 ,
        S_KEEP_ENABLE        => 1           ,
        S_KEEP_WIDTH         => numbyte     ,
        M_DATA_WIDTH         => 1*8         , -- 1 bytes
        M_KEEP_ENABLE        => 0   ,
        M_KEEP_WIDTH         => 1   ,    
        ID_ENABLE            => 0   ,
        ID_WIDTH             => 1   ,
        DEST_ENABLE          => 0   ,
        DEST_WIDTH           => 1   ,
        USER_ENABLE          => 0   ,
        USER_WIDTH           => 1   ,
        RAM_PIPELINE         => 2   ,
        OUTPUT_FIFO_ENABLE   => 0   ,
        FRAME_FIFO           => 0   ,
        USER_BAD_FRAME_VALUE => '0' ,
        USER_BAD_FRAME_MASK  => '0' ,
        DROP_OVERSIZE_FRAME  => 0   ,
        DROP_BAD_FRAME       => 0   ,
        DROP_WHEN_FULL       => 0         
    )
    Port map (
        s_clk                => utx_clock       ,
        s_rst                => rst             ,
        s_axis_tdata         => swaputx_data    ,
        s_axis_tkeep         => (others => '1') ,
        s_axis_tvalid        => utx_valid       ,
        s_axis_tready        => utx_ready       ,
        s_axis_tlast         => '1'             ,
        s_axis_tid           => (others => '0') ,
        s_axis_tdest         => (others => '0') ,
        s_axis_tuser         => (others => '0') ,
        m_clk                => clk             ,
        m_rst                => rst             ,
        m_axis_tdata         => fifo_wr_data    ,
        m_axis_tkeep         => open            ,
        m_axis_tvalid        => fifo_wr_en      ,
        m_axis_tready        => fifo_ready      ,
        m_axis_tlast         => open            ,
        m_axis_tid           => open            ,
        m_axis_tdest         => open            ,
        m_axis_tuser         => open
    );

txdatafifo_inst2: fallthrough_small_fifo
 generic map(
	  FORCE_DISTRIBUTED   => FORCE_DISTRIBUTED  ,
	  WIDTH               => DATA_WIDTH         ,
	  MAX_DEPTH_BITS      => MAX_DEPTH_BITS     ,
	  PROG_FULL_THRESHOLD => PROG_FULL_THRESHOLD
	  )
 port map(
	  din         => fifo_wr_data  ,
	  wr_en       => fifo_wr_en    ,
	  rd_en       => fifo_rd_en    ,
	  dout        => fifo_rd_data  ,
	  full        => open          ,
	  nearly_full => fifo_full     ,
	  prog_full   => open          ,
	  empty       => fifo_empty    ,
	  reset       => rst           ,
	  clk         => clk       
	  );
	  
fifo_ready <= not fifo_full;

--how to read fifo? (UART_TX not busy) and (fifo not empty)
fifo_rd_en  <= '1' when tx_busy = '0' and fifo_empty = '0' else '0';
--uart tx enable when have read fifo
tx_ena      <= fifo_rd_en;
--uart tx data is data read from fifo
tx_data     <= fifo_rd_data;

end Behavioral;
