#include "shared-bindings/board/__init__.h"

STATIC const mp_rom_map_elem_t board_module_globals_table[] = {
  
  { MP_ROM_QSTR(MP_QSTR_POW_DET), MP_ROM_PTR(&pin_P0_03) },
  
  { MP_ROM_QSTR(MP_QSTR_COIN_O_0), MP_ROM_PTR(&pin_P1_04) },
  { MP_ROM_QSTR(MP_QSTR_COIN_O_1), MP_ROM_PTR(&pin_P1_03) },
  { MP_ROM_QSTR(MP_QSTR_COIN_I_0), MP_ROM_PTR(&pin_P1_05) },
  { MP_ROM_QSTR(MP_QSTR_COIN_I_1), MP_ROM_PTR(&pin_P1_06) },
  { MP_ROM_QSTR(MP_QSTR_COIN_PU), MP_ROM_PTR(&pin_P1_07) },
  { MP_ROM_QSTR(MP_QSTR_BILL_I_0), MP_ROM_PTR(&pin_P1_11) },

  
  { MP_ROM_QSTR(MP_QSTR_TCKT_DRV_O_0), MP_ROM_PTR(&pin_P0_11) },
  { MP_ROM_QSTR(MP_QSTR_TCKT_DRV_O_1), MP_ROM_PTR(&pin_P0_12) },
  { MP_ROM_QSTR(MP_QSTR_TCKT_DRV_I_0), MP_ROM_PTR(&pin_P0_09) },
  { MP_ROM_QSTR(MP_QSTR_TCKT_DRV_I_1), MP_ROM_PTR(&pin_P0_10) },
  { MP_ROM_QSTR(MP_QSTR_TCKT_SEL_0), MP_ROM_PTR(&pin_P0_24) },
  { MP_ROM_QSTR(MP_QSTR_NOTCH_O_0), MP_ROM_PTR(&pin_P1_01) },
  { MP_ROM_QSTR(MP_QSTR_NOTCH_O_1), MP_ROM_PTR(&pin_P1_02) },
  { MP_ROM_QSTR(MP_QSTR_NOTCH_I_0), MP_ROM_PTR(&pin_P1_14) },
  { MP_ROM_QSTR(MP_QSTR_NOTCH_I_1), MP_ROM_PTR(&pin_P1_10) },
  
  { MP_ROM_QSTR(MP_QSTR_PRIZE_I_0), MP_ROM_PTR(&pin_P1_13) },
  
  { MP_ROM_QSTR(MP_QSTR_INHIBIT_I_0), MP_ROM_PTR(&pin_P1_15) },
  { MP_ROM_QSTR(MP_QSTR_INHIBIT_O_0), MP_ROM_PTR(&pin_P1_00) },

  { MP_ROM_QSTR(MP_QSTR_SEG_A), MP_ROM_PTR(&pin_P0_25) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_B), MP_ROM_PTR(&pin_P0_26) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_C), MP_ROM_PTR(&pin_P0_27) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_D), MP_ROM_PTR(&pin_P0_28) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_E), MP_ROM_PTR(&pin_P0_29) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_F), MP_ROM_PTR(&pin_P0_30) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_G), MP_ROM_PTR(&pin_P0_31) },  // Low is on.
  { MP_ROM_QSTR(MP_QSTR_SEG_DP), MP_ROM_PTR(&pin_P0_02) },  // Low is on.

  { MP_ROM_QSTR(MP_QSTR_PROM_SCK), MP_ROM_PTR(&pin_P0_23) },
  { MP_ROM_QSTR(MP_QSTR_PROM_MOSI), MP_ROM_PTR(&pin_P0_20) },
  { MP_ROM_QSTR(MP_QSTR_PROM_MISO), MP_ROM_PTR(&pin_P0_19) },
  { MP_ROM_QSTR(MP_QSTR_PROM_CS), MP_ROM_PTR(&pin_P0_22) },
  { MP_ROM_QSTR(MP_QSTR_PROM_WP), MP_ROM_PTR(&pin_P0_21) },
  { MP_ROM_QSTR(MP_QSTR_PROM_HOLD), MP_ROM_PTR(&pin_P0_17) },

  { MP_ROM_QSTR(MP_QSTR_SCK), MP_ROM_PTR(&pin_P0_07) },
  { MP_ROM_QSTR(MP_QSTR_MOSI), MP_ROM_PTR(&pin_P0_05) },
  { MP_ROM_QSTR(MP_QSTR_MISO), MP_ROM_PTR(&pin_P0_06) },
  { MP_ROM_QSTR(MP_QSTR_INT0_N), MP_ROM_PTR(&pin_P0_04) },
  { MP_ROM_QSTR(MP_QSTR_RST0_N), MP_ROM_PTR(&pin_P0_08) },
  { MP_ROM_QSTR(MP_QSTR_SCS0_N), MP_ROM_PTR(&pin_P1_12) },

  { MP_ROM_QSTR(MP_QSTR_TX), MP_ROM_PTR(&pin_P1_08) },
  { MP_ROM_QSTR(MP_QSTR_RX), MP_ROM_PTR(&pin_P1_09) },
  
  { MP_ROM_QSTR(MP_QSTR_TX0), MP_ROM_PTR(&pin_P0_15) },
  { MP_ROM_QSTR(MP_QSTR_RX0), MP_ROM_PTR(&pin_P0_14) },
  { MP_ROM_QSTR(MP_QSTR_CTS0), MP_ROM_PTR(&pin_P0_16) },
  { MP_ROM_QSTR(MP_QSTR_RTS0), MP_ROM_PTR(&pin_P0_13) },

  { MP_ROM_QSTR(MP_QSTR_UART), MP_ROM_PTR(&board_uart_obj) },
  { MP_ROM_QSTR(MP_QSTR_SPI), MP_ROM_PTR(&board_spi_obj) },


  // BUT this is the RESET pin so we can't really use it.
  { MP_ROM_QSTR(MP_QSTR_BUTTON), MP_ROM_PTR(&pin_P0_18) },  // Low is pressed.
};

MP_DEFINE_CONST_DICT(board_module_globals, board_module_globals_table);
