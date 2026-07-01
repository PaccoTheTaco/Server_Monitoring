import asyncio
import time
import psutil

async def dummy_task():
    start = time.time()
    await asyncio.sleep(0.1)
    end = time.time()
    return end - start

async def run_blocking():
    print("--- BLOCKING BASELINE ---")
    task = asyncio.create_task(dummy_task())

    # Yield to event loop to let dummy_task start
    await asyncio.sleep(0.01)

    # This will block the event loop
    start_psutil = time.time()
    cpu_usage = psutil.cpu_percent(interval=1)
    end_psutil = time.time()

    task_duration = await task

    print(f"psutil call duration: {end_psutil - start_psutil:.4f}s")
    print(f"Dummy task duration (expected ~0.1s): {task_duration:.4f}s")

    if task_duration > 0.5:
        print("Event loop was blocked! The dummy task was delayed.")
    else:
        print("Event loop was NOT blocked.")

async def run_non_blocking():
    print("\n--- NON-BLOCKING (OPTIMIZED) ---")
    task = asyncio.create_task(dummy_task())

    # Yield to event loop to let dummy_task start
    await asyncio.sleep(0.01)

    # This will run in a separate thread, freeing the event loop
    start_psutil = time.time()
    cpu_usage = await asyncio.to_thread(psutil.cpu_percent, interval=1)
    end_psutil = time.time()

    task_duration = await task

    print(f"psutil call duration: {end_psutil - start_psutil:.4f}s")
    print(f"Dummy task duration (expected ~0.1s): {task_duration:.4f}s")

    if task_duration > 0.5:
        print("Event loop was blocked! The dummy task was delayed.")
    else:
        print("Event loop was NOT blocked.")

async def main():
    await run_blocking()
    await run_non_blocking()

if __name__ == "__main__":
    asyncio.run(main())
