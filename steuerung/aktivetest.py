import output
import time
current_milli_time = lambda: int(round(time.time() * 1000))
start_zeit = current_milli_time() + 10000

pump = output.pump(
    actor_id=1,
    run_pin=26,
    ready_pin=13,
    feedback_pin=19
)
gesetzt = 0
pump.set_run(0)
while 1:
    if start_zeit < current_milli_time() and not gesetzt:
        pump.set_run(1)

    print(pump.get_ready(), pump.get_feedback())
    time.sleep(0.5)
