from pydantic import BaseModel
from typing import Union

class ResultObject(BaseModel):
    result: Union[list, dict]
            
class Country(BaseModel):
    Code: str
    Name: str
    Continent: str
    Region: str
    SurfaceArea: float
    IndepYear: str
    Population: int
    LifeExpectancy: float
    GNP: float
    GNPOld: float
    LocalName: str
    GovernmentForm: str
    HeadOfState: str
    Capital: int
    Code2: str


class City(BaseModel):
    ID: int
    Name: str
    CountryCode: str
    District: str
    Population: int


class CountryLanguage(BaseModel):
    CountryCode: str
    Language: str
    IsOfficial: str
    Percentage: float
