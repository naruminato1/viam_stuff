import asyncio

from viam.components.base import Base
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


# python3 -m venv .venv
# source .venv/bin/activate

# pip install viam-sdk

#sudo apt update
# sudo apt install git

async def connect():
    opts = RobotClient.Options.with_api_key(
        # Replace "<API-KEY>" (including brackets) with your machine's API key
        api_key='daf7ivgrdldo7egh6dfi9o2u4gs065c8',
        # Replace "<API-KEY-ID>" (including brackets) with your machine's
        # API key ID
        api_key_id='1674f5cf-85e2-488c-bf27-6f6ecfec0086'
    )
    return await RobotClient.at_address('mrrover-main.dpyc8pclwr.viam.cloud', opts)


async def moveInSquare(base):
    for _ in range(4):
        # moves the rover forward 500mm at 500mm/s
        await base.move_straight(velocity=500, distance=500)
        print("move straight")
        # spins the rover 90 degrees at 100 degrees per second
        await base.spin(velocity=100, angle=90)
        print("spin 90 degrees")


async def main():
    machine = await connect()

    roverBase = Base.from_robot(machine, 'viam_base')

    # Move the rover in a square
    await moveInSquare(roverBase)

    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())

