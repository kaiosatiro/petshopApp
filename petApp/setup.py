from setuptools import setup

setup(
    name="petShopApp",
    version="1.0.0",
    description="",
    # long_description=README,
    # long_description_content_type="text/markdown",
    url="https://github.com/kaiosatiro/petshopApp",
    author="Caio Satiro",
    author_email="kaiosatiro@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["source"],
    include_package_data=True,
    install_requires=[
        "CTkMessagebox", "CTkTable", "customtkinter", "Pillow", "pandas"
    ],
    entry_points={"console_scripts": ["petshopapp=petApp.app:main"]},
)
