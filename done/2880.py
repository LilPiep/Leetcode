import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.query('student_id == 101').iloc[:, [1, 2]]