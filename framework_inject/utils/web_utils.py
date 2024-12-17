import os
import requests

from logger.logger import Logger


class WebUtils(Logger):
    def __init__(self, logger=__file__):
        super().__init__(logger)

    def download_image(self, image_url, save_dir, image_name='blog.png'):
        """
        This method downloads an image to specified save_dir. Not used in a project,
         but may be helpful if image processing will be added
        :param image_url:
        :param save_dir:
        :param image_name:
        :return: image_name or None
        """
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            # image_name = os.path.basename(image_url)
            image_path = os.path.join(save_dir, image_name)
            with open(image_path, 'wb') as file:
                file.write(response.content)

            return image_name
        except Exception as e:
            print(f"Error downloading image from {image_url}: {e}")
            return None
