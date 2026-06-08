from pydantic import BaseModel


class CareerProfileResponse(BaseModel):

    skills: list[str]

    projects: list[str]

    education: list[str]

    experience: list[str]