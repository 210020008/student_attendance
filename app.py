from flask import Flask,render_template_string,send_file, render_template, request
import pandas as pd
import os
from urllib.parse import unquote

app = Flask(__name__)

index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV Processing</title>
    <link rel="stylesheet" href="styles.css">
</head>
<style>
@import url( 
"https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"); 

* { 
	margin: 0; 
	padding: 0; 
	box-sizing: border-box; 
	font-family: "Poppins", sans-serif; 
} 

body { 
	background-color: #000000; 
	background-image: linear-gradient(bottom, 
									#000058 60%, 
									#000033 40%); 
} 

header { 
	width: 100%; 
	height: 90px; 
	position: absolute; 
	z-index: 100; 
	display: flex; 
	flex-direction: column; 
	align-items: center; 
	justify-content: center; 
	background-color: #ffffff; 
} 

.heading { 
	color: green; 
} 

.title { 
	font-weight: 400; 
	letter-spacing: 1.5px; 
} 

ul.fireflies { 
	list-style: none; 
} 

li { 
	border-radius: 50%; 
	background-color: rgb(255, 255, 73); 
	background-image: radial-gradient(rgb(249, 206, 36) 5%, 
									rgb(254, 179, 4) 25%, 
									rgb(252, 191, 7) 60%); 
	box-shadow: 0 0 5px 2px rgb(250, 193, 93), 
				0 0 20px 10px rgb(255, 228, 140), 
				0 0 40px 15px rgb(255, 219, 41); 
	height: 5px; 
	width: 5px; 
	top: -20px; 
	position: absolute; 
	animation: leftright 24s infinite cubic-bezier(0.39, 0, 0.63, 1), 
		updown 8s infinite 1.25s cubic-bezier(0.39, 0, 0.63, 1), 
		blinking 3s infinite; 
} 

/* first 10 */
li:nth-of-type(1) { 
	animation-delay: 1s; 
	animation-duration: 65s, 81s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(2) { 
	animation-delay: 0.5s; 
	animation-duration: 80s, 75s, 0.01s; 
} 

li:nth-of-type(3) { 
	animation-delay: 1.5s; 
	animation-duration: 70s, 60s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(4) { 
	animation-delay: 2.5s; 
	animation-duration: 90s, 80s, 0.01s; 
} 

li:nth-of-type(5) { 
	animation-delay: 0.3s; 
	animation-duration: 55s, 75s, 0.01s; 
} 

li:nth-of-type(6) { 
	animation-delay: 2.2s; 
	animation-duration: 79s, 63s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(7) { 
	animation-delay: 0.9s; 
	animation-duration: 70s, 80s, 0.01s; 
} 

li:nth-of-type(8) { 
	animation-delay: 1.6s; 
	animation-duration: 50s, 40s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(9) { 
	animation-delay: 1.8s; 
	animation-duration: 77s, 88s, 0.01s; 
} 

li:nth-of-type(10) { 
	animation-delay: 3s; 
	animation-duration: 87s, 73s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

/* last 10 */
li:nth-of-type(11) { 
	animation-delay: 1s; 
	animation-duration: 60s, 78s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(12) { 
	animation-delay: 0.5s; 
	animation-duration: 85s, 80s, 0.01s; 
} 

li:nth-of-type(13) { 
	animation-delay: 1.5s; 
	animation-duration: 75s, 66s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(14) { 
	animation-delay: 2.5s; 
	animation-duration: 87s, 75s, 0.01s; 
} 

li:nth-of-type(15) { 
	animation-delay: 0.3s; 
	animation-duration: 69s, 85s, 0.01s; 
} 

li:nth-of-type(16) { 
	animation-delay: 2.2s; 
	animation-duration: 80s, 77s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(17) { 
	animation-delay: 0.9s; 
	animation-duration: 65s, 88s, 0.01s; 
} 

li:nth-of-type(18) { 
	animation-delay: 1.6s; 
	animation-duration: 59s, 63s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

li:nth-of-type(19) { 
	animation-delay: 1.8s; 
	animation-duration: 88s, 79s, 0.01s; 
} 

li:nth-of-type(20) { 
	animation-delay: 3s; 
	animation-duration: 59s, 75s, 0.01s; 
	animation-fill-mode: backwards, backwards; 
} 

/* animations */

/* It will create the left right movement */
@keyframes leftright { 

	0%, 
	100% { 
		left: 80%; 
	} 

	16.666% { 
		left: 95%; 
	} 

	33.333% { 
		left: 10%; 
	} 

	50% { 
		left: 60%; 
	} 

	66.666% { 
		left: 70%; 
	} 

	83.333% { 
		left: 5%; 
	} 
} 

/* It will create the up down movement */
@keyframes updown { 

	0%, 
	100% { 
		top: 10px; 
	} 

	25% { 
		top: 90%; 
	} 

	50% { 
		top: 50%; 
	} 

	75% { 
		top: 95%; 
	} 
} 

/* It will create the blinking effect */
@keyframes blinking { 

	0%, 
	100% { 
		box-shadow: 0 0 5px 2px rgb(250, 193, 93), 
					0 0 10px 5px rgb(255, 242, 63), 
					0 0 30px 10px rgb(255, 219, 41); 
		height: 0; 
		width: 0; 
	} 

	50% { 
		box-shadow: 0 0 5px 2px rgb(250, 193, 93), 
					0 0 20px 10px rgb(255, 228, 140), 
					0 0 40px 15px rgb(255, 219, 41); 
	} 

	75% { 
		box-shadow: 0 0 0px 0px rgb(250, 193, 93), 
					0 0 0px 0px rgb(255, 228, 140), 
					0 0 0px 0px rgb(255, 219, 41); 
	} 
}


/* Apply animation and color transition to the heading */
.bounce-color {
    display: inline-block;
    animation: bounce 2s infinite; /* Bounce animation with 2 seconds duration */
    transition: color 0.5s ease; /* Smooth color transition over 0.5 seconds */ /* Initial color */
    color: #FB9AD1;
    font-family: cursive;
}

/* Change color smoothly */
.bounce-color:hover {
    color: #ECCA9C; /* Color change on hover */
}
body {
    font-family: "Comic Sans MS", cursive;
    color : #C6EBC5;
    margin: 0;
    padding: 0;
	text-align: center;
}

h1 {
    margin-top: 50px; /* Adjust top margin for heading */
}

form {
    margin-top: 20px; /* Adjust top margin for form */
}
.button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    text-transform: uppercase;
    color: #D20062;
    background-color: #97E7E1;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 4px 6px #FFC94A;
  }
/* Pulse animation */
@keyframes pulse {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
    100% {
      transform: scale(1);
    }
  }
  /* Apply pulse animation on button hover */
.button:hover {
    animation: pulse 0.6s infinite alternate;
  }
</style>
<body>
    <h1 class="bounce-color">Student Attendance Data</h1>
    <form id="csvForm" method="post" enctype="multipart/form-data">
        <input type="file" name="csv_file" accept=".csv">
        <button class="button" type="submit">Process CSV</button>
    </form>
    <div id="result"></div>
    <ul class="fireflies"> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
        <li></li> 
    </ul> 
    <script>
        document.getElementById('csvForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData();
            formData.append('csv_file', document.querySelector('input[type=file]').files[0]);
            
            const response = await fetch('/process_csv', {
                method: 'POST',
                body: formData
            });

            const csvData = await response.text();
            document.getElementById('result').innerText = csvData;
        });
    </script>
</body>
</html>

'''


@app.route('/')
def index():
    return render_template_string(index_html)


@app.route('/process_csv', methods=['POST'])
def process_csv():
    if 'csv_file' not in request.files:
        return "No file part"
    
    file = request.files['csv_file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        df = pd.read_csv(file)
        
        num_columns = df.shape[1]
        num_rows = df.shape[0]
        
        percentage_list = []
        marks_alloted = []

        student_id = []
        student_id = df['ROLL NUMBER']

        for r in range(num_rows):
            value = 0
            for c in range(num_columns):
                if df.iloc[r, c] == 'present':
                    value += 1
            marks_alloted.append(value * 0.5)
            value = value / (num_columns - 1) * 100
            percentage_list.append(value)

        df['percentage_attendance'] = percentage_list
        df['marks_alloted'] = marks_alloted
        dx_grade = []

        for e,j in zip(percentage_list,student_id):
            if e<80:
                dx_grade.append(j)


        # Get the directory where app.py is located
        directory = os.path.dirname(os.path.realpath(__file__))
        
        # Save the modified DataFrame to a new CSV file in the same directory
        output_path = os.path.join(directory, 'processed_data.csv')
        df.to_csv(output_path, index=False)
        student_details = "\n\nStudent Details:\n" + ''.join([f"Id: {student_id}\nAttendance Percenatge: {percentage}\nMarks for attendance : {marks}\n\n\n" for student_id, percentage, marks in zip(student_id, percentage_list, marks_alloted)])

        #return f"\nProcessed and Stored Successfully.\n Roll Number of students with attendance less than 80%:\n {', '.join(map(str, dx_grade))}"
        return (f"\nProcessed and Stored Successfully.\n Roll Number of students with attendance less than 80%:\n {', '.join(map(str, dx_grade))}" +
        f"{student_details}")

        

if __name__ == '__main__':
    app.run(debug=True)
