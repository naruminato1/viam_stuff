import asyncio
from viam.components.camera import Camera
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials

async def connect():
    opts = RobotClient.Options.with_api_key(
        # Replace "<API-KEY>" (including brackets) with your machine's API key
        api_key='daf7ivgrdldo7egh6dfi9o2u4gs065c8',
        # Replace "<API-KEY-ID>" (including brackets) with your machine's
        # API key ID
        api_key_id='1674f5cf-85e2-488c-bf27-6f6ecfec0086'
    )
    return await RobotClient.at_address('mrrover-main.dpyc8pclwr.viam.cloud', opts)


async def take_and_save_picture(camera_name, save_path):
    robot = await connect()

    # Get the camera component
    camera = Camera.from_robot(robot, camera_name)

    # Take a picture
    image = await camera.get_image()
    print("Picture taken!")

    # Save the image to the specified path
    with open(save_path, 'wb') as f:
        f.write(image)
    print(f"Picture saved to {save_path}")

    await robot.close()

if __name__ == "__main__":
    camera_name = "cam"  
    save_path = "/home/rover/Pictures/captured_image.jpg"  # Path to save the image

    asyncio.run(take_and_save_picture(camera_name, save_path))