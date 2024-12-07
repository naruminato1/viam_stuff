import asyncio
from viam.components.camera import Camera
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials

async def connect():
    opts = RobotClient.Options.with_api_key(
        api_key='1b4c119c-f2ea-4040-a84c-75af25c66de5',
        api_key_id='1674f5cf-85e2-488c-bf27-6f6ecfec0086'
    )
    return await RobotClient.at_address('my-rover.viam.cloud', opts)

# async def take_and_save_picture(camera_name, save_path):
#     robot = await connect()

#     # Get the camera component
#     camera = Camera.from_robot(robot, camera_name)

#     # Take a picture
#     image = await camera.get_image()
#     print("Picture taken!")

#     # Save the image to the specified path
#     with open(save_path, 'wb') as f:
#         f.write(image.content)  # Use `content` to get the bytes
#     print(f"Picture saved to {save_path}")

#     await robot.close()

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
    camera_name = "cam"  # Replace with your camera's name in the Viam Console
    save_path = "/home/rover/Pictures/captured_image.jpg"  # Replace with the desired save path

    asyncio.run(take_and_save_picture(camera_name, save_path))

    