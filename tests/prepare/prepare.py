import multiprocessing
import os

def run_script(command):
    os.system(command)

if __name__ == "__main__":
    # Run the following scripts in parallel
    commands = [
        "python3 -m tests.prepare.set_general_tests",
        "python3 -m tests.prepare.set_share_tests",
        "python3 -m tests.prepare.set_emissions_tests",
        "python3 -m tests.prepare.set_removals_tests"
        "python3 -m tests.prepare.set_potential_tests"
    ]

    # To run in parallel, we need to create a process for each command
    processes = [multiprocessing.Process(target=run_script, args=(command,)) for command in commands]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
