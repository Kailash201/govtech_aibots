### Developer Guide

This developer guide provides a overview of the backend application. The api ednpoints follows the given backend documentation closely.

The endpoints and its logic can be found at the **main.py** file. 

The **database.py** sets connection to mongodb via beanie.

The **tools.py** holds tool functions for the agent.

Several classes to created to model certain objects. Below are details on these classses:

- **Agent Class UML Diagram:**
![Agent Class UML](/docs/agent_model.png)

- **Beanie models Class UML Diagram**:
![Beanie Models UML](/docs/beanie_models.png)
*All the clases here inherit from Beanie's Document class

- **Filetype Models Class UML Diagram:**
![FileType Class Models UML](/docs/file_models.png)

The **tests** folder holds test cases for the app.


#### Possible improvements
In the current design, the files and websites are stored into the database when user creates agent.

Due to this, the user does not need send over files again into the put request for extracting file text, as the files are already stored into the db.
