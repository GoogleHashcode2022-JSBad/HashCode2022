for project in self.projects:
            for i, skill_name in enumerate(project.skills.keys()):
                for contributer in self.contributers:
                    if skill_name in contributer.skills:
                        if contributer.skills[skill_name] >= project.skills[skill_name]:
                            project.contributers[i] = contributer
                            if contributer.skills[skill_name] == project.skills[skill_name]:
                                contributer.skills[skill_name] += 1
                            break
            if len(project.contributers) != project.num_roles:
                # Find a contributer that has skill one less than project skill required given that another
