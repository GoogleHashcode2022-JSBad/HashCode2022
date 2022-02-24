class Solution:
    def __init__(self):
        self.C = None
        self.P = None
        self.contributers = []
        self.projects = []

    
    def get_input(self, file_name):
        with open(file_name, "r") as f:
            C, P = f.readline().split()
            C = int(C)
            P = int(P)
            self.C = C
            self.P = P

            for contributer in range(C):
                contributer_name, num_skills = f.readline().split()
                num_skills = int(num_skills)
                contributer = Contributer(contributer_name, num_skills)

                for i in range(num_skills):
                    skill_name, skill_level = f.readline().strip().split()
                    skill_level = int(skill_level)
                    contributer.skills[skill_name] = skill_level

                self.contributers.append(contributer)
            
            for project in range(P):
                project_name, num_days, score_completion, best_before, num_roles = f.readline().split()
                num_days = int(num_days)
                score_completion = int(score_completion)
                best_project = int(best_before)
                num_roles = int(num_roles)
                project = Project(project_name, num_days, score_completion, best_before, num_roles)


                for i in range(num_roles):
                    skill_name, level_required = f.readline().split()
                    level_required = int(level_required)
                    project.skills[skill_name] = level_required

                self.projects.append(project)


    def solve(self):
        for project in self.projects:
            contributers_copy = set(self.contributers)
            for skill_required in project.skills:
                for contributer in contributers_copy:
                    if skill_required in contributer.skills:
                        if contributer.skills[skill_required] >= project.skills[skill_required]:
                            project.contributers.append(contributer)
                            contributers_copy.remove(contributer)
                            break
                    


    def write_output(self):
        global test_case_number
        file_name = "output" + str(test_case_number) + ".txt"
        with open(file_name, "w") as f:
            f.write(str(self.P) + "\n")
            for project in self.projects:
                f.write(project.name + "\n")
                for contributer in project.contributers[:-1]:
                    f.write(contributer.name + " ")
                f.write(project.contributers[-1].name + "\n")
        #         from random import choice
        #         copy = set(self.contributers)
        #         for i in range(project.num_roles - 1):
        #             f.write(str(copy.pop().name) + " ")
        #         f.write(str(copy.pop().name) + "\n")


            

class Project:
    def __init__(self, name, num_days, score_completion, best_before, num_roles):
        self.name = name
        self.num_days = num_days
        self.score_completion = score_completion
        self.best_before = best_before
        self.num_roles = num_roles
        self.skills = {}
        self.contributers = []

        


class Contributer:
    def __init__(self, name, num_skills):
        self.name = name
        self.num_skills = num_skills
        self.skills = {}


if __name__ == "__main__":
    test_case_number = 1
    file_names = ["input_data/a_an_example.in.txt", "input_data/b_better_start_small.in.txt", "input_data/c_collaboration.in.txt", "input_data/d_dense_schedule.in.txt", "input_data/e_exceptional_skills.in.txt", "input_data/f_find_great_mentors.in.txt"]
    for file_name in file_names:
        solution = Solution()
        solution.get_input(file_name)
        solution.solve()
        solution.write_output()
        test_case_number += 1