class CodeModule:
    def __init__(self):
        self.dependencies = []
        self.test_coverage = 0.0
        self.documentation_quality = 0.0
        self.lines_of_code = 0
        self.complexity = 0
        self.hours_technical_debt = 0

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def develop_feature(self, feature, developers):
        # Here is where most of the simulation logic happens
        self.hours_technical_debt += feature.estimated_hours
        self.lines_of_code += feature.lines_of_code
        self.complexity += feature.complexity
        for developer in developers:
            developer.burnout += (
                feature.estimated_hours / len(developers)
            ) - developer.skill
            if self in developer.specialized_code_modules:
                developer.burnout -= 0.1 * feature.estimated_hours / len(developers)
            developer.skill += feature.complexity / len(developers)
            developer.specialize_code_module(self)

    def test_feature(self, feature, testers):
        # Here is where most of the simulation logic happens
        self.test_coverage += feature.test_coverage
        self.documentation_quality += feature.documentation_quality
        for tester in testers:
            tester.burnout += (feature.estimated_hours / len(testers)) - tester.skill
            tester.skill += feature.complexity / len(testers)
            tester.specialize_code_module(self)

    def __repr__(self):
        return f"CodeModule(dependencies={self.dependencies}, test_coverage={self.test_coverage}, documentation_quality={self.documentation_quality}, lines_of_code={self.lines_of_code}, complexity={self.complexity}, hours_technical_debt={self.hours_technical_debt})"
