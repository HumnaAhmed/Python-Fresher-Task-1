
class StudentManager:

    def __init__(self, course_name):
        self.course_name = course_name
        self.__students = []

    def add_student(self, name, score):
        if 0 <= score <= 100:
            self.__students.append({"name": name, "score": score})
            print(f"[SUCCESS] Added {name} (Score: {score}) to {self.course_name}")
        else:
            raise ValueError("Score must be between 0 and 100")

    def get_top_performers(self, threshold=80):
        return [s["name"] for s in self.__students if s["score"] >= threshold]


def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("[ERROR] Division by zero is undefined.")
        return None
    except TypeError:
        print("[ERROR] Both inputs must be numerical.")
        return None
    else:
        print(f"[RESULT] {numerator} / {denominator} = {result}")
        return result
    finally:
        print("[LOG] Division operation completed.")


if __name__ == "__main__":
    print("=== TASK 2: CORE CONCEPTS & SKILLS EXECUTION ===")

    manager = StudentManager("Python Development")
    manager.add_student("Humna", 95)
    manager.add_student("Ali", 78)
    manager.add_student("Sara", 88)

    top_students = manager.get_top_performers(80)
    print(f"Top Performers (Score >= 80): {top_students}")

    print("\n=== EXCEPTION HANDLING DEMO ===")
    safe_divide(100, 5)
    safe_divide(10, 0)

    print("\n=== PROCESS COMPLETED SUCCESSFULLY ===")