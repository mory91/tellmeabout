from typing import Iterable, Tuple

from linkedin_api import Linkedin  # type: ignore

api = Linkedin("USERNAME", "PASSWORD")


def search_poeple(query: str) -> Iterable[dict]:
    """Search people with the given query in linkedin network.
    The query should contain text only related to the person not any else text

    :param query: string to search with in linkedin
    :type query: str

    :return: Returns the urn_id of the user which is the unique user identifier
    in linkedin
    :rtype: str"""

    results = api.search_people(query, limit=5)
    return results


def scrape_linikedin_profile(linkedin_profile_urn_id: str) -> Tuple[dict, str]:
    """scrape informarion from linkedin profiles,
    Manually scrape information from linkedin profie

    :param linkedin_profile_urn_id: urn_id (unique user id) of linkedin user
    :type linkedin_profile_urn_id: str

    :return: Returns the linkedin user data
    :rtype: dict"""

    data = api.get_profile(urn_id=linkedin_profile_urn_id)

    photo = f"{data['displayPictureUrl']}{data['img_560_560']}"

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ("people_also_viewed", "certifications")
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data, photo
