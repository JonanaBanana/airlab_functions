from setuptools import find_packages, setup

package_name = 'airlab_functions'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jonathan',
    maintainer_email='jonathan@todo.todo',
    description='A package for capturing and preparing data for gaussian splatting reconstruction without SfM from Colmap',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'isaac_pc_cat = airlab_functions.isaac_pc_cat:main',
        'isaac_image_capture = airlab_functions.isaac_image_capture:main',
        'rgb_pcl_capture = airlab_functions.rgb_pcl_capture:main',
        'pc_repub = airlab_functions.pc_repub:main',
        'rgb_pcl_viz = airlab_functions.rgb_pcl_visualizer:main',
        'image_transform_capture = airlab_functions.rgb_transf_capture:main',
        'pointcloud_accumulator = airlab_functions.pointcloud_accumulator:main',
        'fast_lio_capture = airlab_functions.fast_lio_img_transf_capture:main'
        ],
    },
)
