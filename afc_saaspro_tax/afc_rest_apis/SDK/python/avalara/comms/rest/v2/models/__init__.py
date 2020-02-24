# coding: utf-8

# flake8: noqa
"""
    SaasPro

    APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from avalara.comms.rest.v2.models.address import Address
from avalara.comms.rest.v2.models.billing_period import BillingPeriod
from avalara.comms.rest.v2.models.bundle_config import BundleConfig
from avalara.comms.rest.v2.models.bundle_item import BundleItem
from avalara.comms.rest.v2.models.calc_taxes_request import CalcTaxesRequest
from avalara.comms.rest.v2.models.calc_taxes_response import CalcTaxesResponse
from avalara.comms.rest.v2.models.commit_request import CommitRequest
from avalara.comms.rest.v2.models.commit_response import CommitResponse
from avalara.comms.rest.v2.models.company_data import CompanyData
from avalara.comms.rest.v2.models.configuration import Configuration
from avalara.comms.rest.v2.models.error import Error
from avalara.comms.rest.v2.models.exclusion import Exclusion
from avalara.comms.rest.v2.models.exclusion_config import ExclusionConfig
from avalara.comms.rest.v2.models.geo_batch_download_response import GeoBatchDownloadResponse
from avalara.comms.rest.v2.models.geo_batch_log import GeoBatchLog
from avalara.comms.rest.v2.models.geo_batch_log_item import GeoBatchLogItem
from avalara.comms.rest.v2.models.geo_batch_status import GeoBatchStatus
from avalara.comms.rest.v2.models.geo_batch_submit_file_response import GeoBatchSubmitFileResponse
from avalara.comms.rest.v2.models.geocode_request import GeocodeRequest
from avalara.comms.rest.v2.models.geocode_result import GeocodeResult
from avalara.comms.rest.v2.models.inline_object import InlineObject
from avalara.comms.rest.v2.models.invoice import Invoice
from avalara.comms.rest.v2.models.invoice_result import InvoiceResult
from avalara.comms.rest.v2.models.key_value_pair import KeyValuePair
from avalara.comms.rest.v2.models.line_item import LineItem
from avalara.comms.rest.v2.models.line_item_result import LineItemResult
from avalara.comms.rest.v2.models.location import Location
from avalara.comms.rest.v2.models.location_item import LocationItem
from avalara.comms.rest.v2.models.nexus_config import NexusConfig
from avalara.comms.rest.v2.models.override_config import OverrideConfig
from avalara.comms.rest.v2.models.p_code_lookup_request import PCodeLookupRequest
from avalara.comms.rest.v2.models.p_code_lookup_result import PCodeLookupResult
from avalara.comms.rest.v2.models.reporting_information import ReportingInformation
from avalara.comms.rest.v2.models.request_config import RequestConfig
from avalara.comms.rest.v2.models.safe_harbor_override import SafeHarborOverride
from avalara.comms.rest.v2.models.service_info import ServiceInfo
from avalara.comms.rest.v2.models.set_tax_calculation_setting_request import SetTaxCalculationSettingRequest
from avalara.comms.rest.v2.models.status import Status
from avalara.comms.rest.v2.models.summarized_tax import SummarizedTax
from avalara.comms.rest.v2.models.ts_pair_data import TSPairData
from avalara.comms.rest.v2.models.tax import Tax
from avalara.comms.rest.v2.models.tax_bracket import TaxBracket
from avalara.comms.rest.v2.models.tax_calculation_setting_types import TaxCalculationSettingTypes
from avalara.comms.rest.v2.models.tax_calculation_settings_response import TaxCalculationSettingsResponse
from avalara.comms.rest.v2.models.tax_exemption import TaxExemption
from avalara.comms.rest.v2.models.tax_override import TaxOverride
from avalara.comms.rest.v2.models.tax_type_data import TaxTypeData
from avalara.comms.rest.v2.models.traffic_study_override import TrafficStudyOverride
from avalara.comms.rest.v2.models.version_info import VersionInfo
from avalara.comms.rest.v2.models.warning import Warning