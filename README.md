

## ToDoList
````markdown
# ToDoList

A simple and intuitive **To-Do List** web application built with Flask (or specify your framework) that lets users manage daily tasks with ease.


  Features
- Add tasks — Quickly jot down what needs to be done.
- Edit tasks — Modify tasks you've created.
- Delete tasks — Remove obsolete or completed items.
- Mark tasks complete — Easily track what’s done.

 Built With
- Languages: Python, HTML/CSS, (add JS if used)  
- Frameworks/Libraries: Flask (assuming from `app.py`), SQLAlchemy or SQLite (if using `todo.db`), Bootstrap (if any front-end framework)  
- Database:SQLite via `todo.db` (if that's what you’re using)  

  Getting Started

Prerequisites
- Python 3.x  
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sreyoshi244/ToDoList.git
   cd ToDoList
````

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database (if applicable):

   ```bash
   python app.py  # Or use Flask migrations if set up
   ```
5. Run the app:

   ```bash
   python app.py
   ```
6. Visit `http://localhost:5000` in your browser to start managing your tasks.

## Usage

* **Add a task:** Click “Add Task”, fill the form, and submit.
* **Edit/Delete:** Use edit/delete icons next to each task.
* **Mark as completed:** Click the checkbox or “Done” button next to a task to complete it.

*(Adjust directions based on your interface.)*

