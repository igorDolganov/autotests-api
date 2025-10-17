from clients.api_client import APIClient
from httpx import Response
from clients.courses.courses_client import GetCoursesQueryDict
from typing import TypedDict


class CreateExerciseRequestDict(TypedDict):
    """
        Описание структуры запроса на создание списка упражнений.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
        Описание структуры запроса на обновление списка упражнений.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
            Метод создания упражнений
            :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercises_api(self, query: GetCoursesQueryDict) -> Response:
        """
            Метод получения упражнений у конкретного курса
            Переиспользуем класс из Курсов, так как тут нам тоже нужен айди курса
            :param query: айдишник курса по которому получаем упражнения
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
            Метод получения упражнения по его айди
            :param exercise_id: айди упражнения
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
            Метод обновления упражнений
            :param exercise_id: айди упражнения, которое обновляем
            :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
            Метод удаления упражнений
            :param exercise_id: айди упражнения
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
