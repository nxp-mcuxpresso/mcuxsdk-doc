# Example freertos_lpspi fail before the console output

The example freertos_lpspi fails before the message "LPSPI master transfer completed successfully." appears in the console output.

  Console output:

    ```
    FreeRTOS LPSPI example start.
    This example use one lpspi instance as master and another as slave on a single board.
    Master and slave are both use interrupt way.
    Please make sure you make the correct line connection. Basically, the connection is:
    LPSPI_master -- LPSPI_slave
     CLK -- CLK
     PCS -- PCS
     SOUT -- SIN
     SIN -- SOUT
   ```   