from app import api, Resource, Department


@api.route("/api/department")
class DepartmentController(Resource):
    def get(self):
        allDepartment = Department.query.all()

        return allDepartment