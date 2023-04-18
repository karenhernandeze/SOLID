# SOLID Principles 
The purpose of this code was to refactor it fot it to met the SOLID principles. Creating a flexible, scalable, maintainable, and reusable code. 
* **S - Single Responsibility:**

'States that a class should do one thing and therefore it should have only a single reason to change.' (Yiğit Kemal Erinç)

The classes created, only have one responsibility. One to fetch the code, another one to refactor te code in the wanted format and finally to write the data in a csv file.

* **O - Open Closed Principle**

'Requires that classes should be open for extension and closed to modification.' (Yiğit Kemal Erinç)

If we wanted to extract another field with the getters and setters we can extend the class rather than modify the whole class. 
* L - Liskov Substitution Principle
* I - Interface Segregation Principle
* D - Dependency Inversion


# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME
