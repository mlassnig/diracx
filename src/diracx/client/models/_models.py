# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.5, generator: @autorest/python@6.4.11)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BodyAuthToken(_serialization.Model):
    """Body_auth_token.

    All required parameters must be populated in order to send to Azure.

    :ivar grant_type: OAuth2 Grant type. Required.
    :vartype grant_type: ~client.models.BodyAuthTokenGrantType
    :ivar client_id: OAuth2 client id. Required.
    :vartype client_id: str
    :ivar device_code: device code for OAuth2 device flow.
    :vartype device_code: str
    :ivar code: Code for OAuth2 authorization code flow.
    :vartype code: str
    :ivar redirect_uri: redirect_uri used with OAuth2 authorization code flow.
    :vartype redirect_uri: str
    :ivar code_verifier: Verifier for the code challenge for the OAuth2 authorization flow with
     PKCE.
    :vartype code_verifier: str
    """

    _validation = {
        "grant_type": {"required": True},
        "client_id": {"required": True},
    }

    _attribute_map = {
        "grant_type": {"key": "grant_type", "type": "BodyAuthTokenGrantType"},
        "client_id": {"key": "client_id", "type": "str"},
        "device_code": {"key": "device_code", "type": "str"},
        "code": {"key": "code", "type": "str"},
        "redirect_uri": {"key": "redirect_uri", "type": "str"},
        "code_verifier": {"key": "code_verifier", "type": "str"},
    }

    def __init__(
        self,
        *,
        grant_type: "_models.BodyAuthTokenGrantType",
        client_id: str,
        device_code: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        code_verifier: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword grant_type: OAuth2 Grant type. Required.
        :paramtype grant_type: ~client.models.BodyAuthTokenGrantType
        :keyword client_id: OAuth2 client id. Required.
        :paramtype client_id: str
        :keyword device_code: device code for OAuth2 device flow.
        :paramtype device_code: str
        :keyword code: Code for OAuth2 authorization code flow.
        :paramtype code: str
        :keyword redirect_uri: redirect_uri used with OAuth2 authorization code flow.
        :paramtype redirect_uri: str
        :keyword code_verifier: Verifier for the code challenge for the OAuth2 authorization flow with
         PKCE.
        :paramtype code_verifier: str
        """
        super().__init__(**kwargs)
        self.grant_type = grant_type
        self.client_id = client_id
        self.device_code = device_code
        self.code = code
        self.redirect_uri = redirect_uri
        self.code_verifier = code_verifier


class BodyAuthTokenGrantType(_serialization.Model):
    """OAuth2 Grant type."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class HTTPValidationError(_serialization.Model):
    """HTTPValidationError.

    :ivar detail: Detail.
    :vartype detail: list[~client.models.ValidationError]
    """

    _attribute_map = {
        "detail": {"key": "detail", "type": "[ValidationError]"},
    }

    def __init__(
        self, *, detail: Optional[List["_models.ValidationError"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword detail: Detail.
        :paramtype detail: list[~client.models.ValidationError]
        """
        super().__init__(**kwargs)
        self.detail = detail


class InitiateDeviceFlowResponse(_serialization.Model):
    """InitiateDeviceFlowResponse.

    All required parameters must be populated in order to send to Azure.

    :ivar user_code: User Code. Required.
    :vartype user_code: str
    :ivar device_code: Device Code. Required.
    :vartype device_code: str
    :ivar verification_uri_complete: Verification Uri Complete. Required.
    :vartype verification_uri_complete: str
    :ivar verification_uri: Verification Uri. Required.
    :vartype verification_uri: str
    :ivar expires_in: Expires In. Required.
    :vartype expires_in: int
    """

    _validation = {
        "user_code": {"required": True},
        "device_code": {"required": True},
        "verification_uri_complete": {"required": True},
        "verification_uri": {"required": True},
        "expires_in": {"required": True},
    }

    _attribute_map = {
        "user_code": {"key": "user_code", "type": "str"},
        "device_code": {"key": "device_code", "type": "str"},
        "verification_uri_complete": {
            "key": "verification_uri_complete",
            "type": "str",
        },
        "verification_uri": {"key": "verification_uri", "type": "str"},
        "expires_in": {"key": "expires_in", "type": "int"},
    }

    def __init__(
        self,
        *,
        user_code: str,
        device_code: str,
        verification_uri_complete: str,
        verification_uri: str,
        expires_in: int,
        **kwargs: Any
    ) -> None:
        """
        :keyword user_code: User Code. Required.
        :paramtype user_code: str
        :keyword device_code: Device Code. Required.
        :paramtype device_code: str
        :keyword verification_uri_complete: Verification Uri Complete. Required.
        :paramtype verification_uri_complete: str
        :keyword verification_uri: Verification Uri. Required.
        :paramtype verification_uri: str
        :keyword expires_in: Expires In. Required.
        :paramtype expires_in: int
        """
        super().__init__(**kwargs)
        self.user_code = user_code
        self.device_code = device_code
        self.verification_uri_complete = verification_uri_complete
        self.verification_uri = verification_uri
        self.expires_in = expires_in


class JobSearchParams(_serialization.Model):
    """JobSearchParams.

    :ivar parameters: Parameters.
    :vartype parameters: list[str]
    :ivar search: Search.
    :vartype search: list[~client.models.JobSearchParamsSearchItem]
    :ivar sort: Sort.
    :vartype sort: list[~client.models.JobSearchParamsSortItem]
    """

    _attribute_map = {
        "parameters": {"key": "parameters", "type": "[str]"},
        "search": {"key": "search", "type": "[JobSearchParamsSearchItem]"},
        "sort": {"key": "sort", "type": "[JobSearchParamsSortItem]"},
    }

    def __init__(
        self,
        *,
        parameters: Optional[List[str]] = None,
        search: List["_models.JobSearchParamsSearchItem"] = [],
        sort: List["_models.JobSearchParamsSortItem"] = [],
        **kwargs: Any
    ) -> None:
        """
        :keyword parameters: Parameters.
        :paramtype parameters: list[str]
        :keyword search: Search.
        :paramtype search: list[~client.models.JobSearchParamsSearchItem]
        :keyword sort: Sort.
        :paramtype sort: list[~client.models.JobSearchParamsSortItem]
        """
        super().__init__(**kwargs)
        self.parameters = parameters
        self.search = search
        self.sort = sort


class JobSearchParamsSearchItem(_serialization.Model):
    """JobSearchParamsSearchItem."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class JobSearchParamsSortItem(_serialization.Model):
    """JobSearchParamsSortItem."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class JobStatusReturn(_serialization.Model):
    """JobStatusReturn.

    All required parameters must be populated in order to send to Azure.

    :ivar job_id: Job Id. Required.
    :vartype job_id: int
    :ivar status: An enumeration. Required. Known values are: "Running", "Stalled", "Killed",
     "Failed", "RECEIVED", and "Submitting".
    :vartype status: str or ~client.models.JobStatus
    """

    _validation = {
        "job_id": {"required": True},
        "status": {"required": True},
    }

    _attribute_map = {
        "job_id": {"key": "job_id", "type": "int"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(
        self, *, job_id: int, status: Union[str, "_models.JobStatus"], **kwargs: Any
    ) -> None:
        """
        :keyword job_id: Job Id. Required.
        :paramtype job_id: int
        :keyword status: An enumeration. Required. Known values are: "Running", "Stalled", "Killed",
         "Failed", "RECEIVED", and "Submitting".
        :paramtype status: str or ~client.models.JobStatus
        """
        super().__init__(**kwargs)
        self.job_id = job_id
        self.status = status


class JobStatusUpdate(_serialization.Model):
    """JobStatusUpdate.

    All required parameters must be populated in order to send to Azure.

    :ivar job_id: Job Id. Required.
    :vartype job_id: int
    :ivar status: An enumeration. Required. Known values are: "Running", "Stalled", "Killed",
     "Failed", "RECEIVED", and "Submitting".
    :vartype status: str or ~client.models.JobStatus
    """

    _validation = {
        "job_id": {"required": True},
        "status": {"required": True},
    }

    _attribute_map = {
        "job_id": {"key": "job_id", "type": "int"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(
        self, *, job_id: int, status: Union[str, "_models.JobStatus"], **kwargs: Any
    ) -> None:
        """
        :keyword job_id: Job Id. Required.
        :paramtype job_id: int
        :keyword status: An enumeration. Required. Known values are: "Running", "Stalled", "Killed",
         "Failed", "RECEIVED", and "Submitting".
        :paramtype status: str or ~client.models.JobStatus
        """
        super().__init__(**kwargs)
        self.job_id = job_id
        self.status = status


class JobSummaryParams(_serialization.Model):
    """JobSummaryParams.

    All required parameters must be populated in order to send to Azure.

    :ivar grouping: Grouping. Required.
    :vartype grouping: list[str]
    :ivar search: Search.
    :vartype search: list[~client.models.JobSummaryParamsSearchItem]
    """

    _validation = {
        "grouping": {"required": True},
    }

    _attribute_map = {
        "grouping": {"key": "grouping", "type": "[str]"},
        "search": {"key": "search", "type": "[JobSummaryParamsSearchItem]"},
    }

    def __init__(
        self,
        *,
        grouping: List[str],
        search: List["_models.JobSummaryParamsSearchItem"] = [],
        **kwargs: Any
    ) -> None:
        """
        :keyword grouping: Grouping. Required.
        :paramtype grouping: list[str]
        :keyword search: Search.
        :paramtype search: list[~client.models.JobSummaryParamsSearchItem]
        """
        super().__init__(**kwargs)
        self.grouping = grouping
        self.search = search


class JobSummaryParamsSearchItem(_serialization.Model):
    """JobSummaryParamsSearchItem."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class ScalarSearchSpec(_serialization.Model):
    """ScalarSearchSpec.

    All required parameters must be populated in order to send to Azure.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar operator: Operator. Required.
    :vartype operator: ~client.models.ScalarSearchSpecOperator
    :ivar value: Value. Required.
    :vartype value: str
    """

    _validation = {
        "parameter": {"required": True},
        "operator": {"required": True},
        "value": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "operator": {"key": "operator", "type": "ScalarSearchSpecOperator"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(
        self,
        *,
        parameter: str,
        operator: "_models.ScalarSearchSpecOperator",
        value: str,
        **kwargs: Any
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword operator: Operator. Required.
        :paramtype operator: ~client.models.ScalarSearchSpecOperator
        :keyword value: Value. Required.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.operator = operator
        self.value = value


class ScalarSearchSpecOperator(_serialization.Model):
    """Operator."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class SortSpec(_serialization.Model):
    """SortSpec.

    All required parameters must be populated in order to send to Azure.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar direction: Direction. Required.
    :vartype direction: ~client.models.SortSpecDirection
    """

    _validation = {
        "parameter": {"required": True},
        "direction": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "direction": {"key": "direction", "type": "SortSpecDirection"},
    }

    def __init__(
        self, *, parameter: str, direction: "_models.SortSpecDirection", **kwargs: Any
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword direction: Direction. Required.
        :paramtype direction: ~client.models.SortSpecDirection
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.direction = direction


class SortSpecDirection(_serialization.Model):
    """Direction."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class TokenResponse(_serialization.Model):
    """TokenResponse.

    All required parameters must be populated in order to send to Azure.

    :ivar access_token: Access Token. Required.
    :vartype access_token: str
    :ivar expires_in: Expires In. Required.
    :vartype expires_in: int
    :ivar state: State. Required.
    :vartype state: str
    """

    _validation = {
        "access_token": {"required": True},
        "expires_in": {"required": True},
        "state": {"required": True},
    }

    _attribute_map = {
        "access_token": {"key": "access_token", "type": "str"},
        "expires_in": {"key": "expires_in", "type": "int"},
        "state": {"key": "state", "type": "str"},
    }

    def __init__(
        self, *, access_token: str, expires_in: int, state: str, **kwargs: Any
    ) -> None:
        """
        :keyword access_token: Access Token. Required.
        :paramtype access_token: str
        :keyword expires_in: Expires In. Required.
        :paramtype expires_in: int
        :keyword state: State. Required.
        :paramtype state: str
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.state = state


class ValidationError(_serialization.Model):
    """ValidationError.

    All required parameters must be populated in order to send to Azure.

    :ivar loc: Location. Required.
    :vartype loc: list[~client.models.ValidationErrorLocItem]
    :ivar msg: Message. Required.
    :vartype msg: str
    :ivar type: Error Type. Required.
    :vartype type: str
    """

    _validation = {
        "loc": {"required": True},
        "msg": {"required": True},
        "type": {"required": True},
    }

    _attribute_map = {
        "loc": {"key": "loc", "type": "[ValidationErrorLocItem]"},
        "msg": {"key": "msg", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(
        self,
        *,
        loc: List["_models.ValidationErrorLocItem"],
        msg: str,
        type: str,
        **kwargs: Any
    ) -> None:
        """
        :keyword loc: Location. Required.
        :paramtype loc: list[~client.models.ValidationErrorLocItem]
        :keyword msg: Message. Required.
        :paramtype msg: str
        :keyword type: Error Type. Required.
        :paramtype type: str
        """
        super().__init__(**kwargs)
        self.loc = loc
        self.msg = msg
        self.type = type


class ValidationErrorLocItem(_serialization.Model):
    """ValidationErrorLocItem."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class VectorSearchSpec(_serialization.Model):
    """VectorSearchSpec.

    All required parameters must be populated in order to send to Azure.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar operator: Operator. Required.
    :vartype operator: ~client.models.VectorSearchSpecOperator
    :ivar values: Values. Required.
    :vartype values: list[str]
    """

    _validation = {
        "parameter": {"required": True},
        "operator": {"required": True},
        "values": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "operator": {"key": "operator", "type": "VectorSearchSpecOperator"},
        "values": {"key": "values", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        parameter: str,
        operator: "_models.VectorSearchSpecOperator",
        values: List[str],
        **kwargs: Any
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword operator: Operator. Required.
        :paramtype operator: ~client.models.VectorSearchSpecOperator
        :keyword values: Values. Required.
        :paramtype values: list[str]
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.operator = operator
        self.values = values


class VectorSearchSpecOperator(_serialization.Model):
    """Operator."""

    _attribute_map = {}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
