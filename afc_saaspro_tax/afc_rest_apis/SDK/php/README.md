# avalara.comms.rest.v2

APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Build package: org.openapitools.codegen.languages.PhpClientCodegen

## Requirements

PHP 5.5 and later

## Installation & Usage

### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/avalara.comms.rest.v2/vendor/autoload.php');
```

## Tests

To run the unit tests:

```bash
composer install
./vendor/bin/phpunit
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');





$apiInstance = new OpenAPI\Client\Api\CustomizationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requested_client_id = 56; // int | Client id associated with profile(s) to be fetched  Null value will use client id submitting the request or default client id as applicable.
$requested_profile_id = 56; // int | Configuration profile id to be fetched  Use 0 to indicate all profiles  Null value will use profile id from request or 0 if not set.
$item_type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\TaxCalculationSettingTypes(); // \OpenAPI\Client\Model\TaxCalculationSettingTypes | Item Type  Examples:    Configuration, Bundle, Exclusion, Override, All

try {
    $result = $apiInstance->apiV2ProfilesGetProfilesGet($requested_client_id, $requested_profile_id, $item_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CustomizationApi->apiV2ProfilesGetProfilesGet: ', $e->getMessage(), PHP_EOL;
}

?>
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomizationApi* | [**apiV2ProfilesGetProfilesGet**](docs/Api/CustomizationApi.md#apiv2profilesgetprofilesget) | **GET** /api/v2/profiles/GetProfiles | Retrieves one or more profiles with associated settings and configurable items
*CustomizationApi* | [**apiV2ProfilesSetBundlesPost**](docs/Api/CustomizationApi.md#apiv2profilessetbundlespost) | **POST** /api/v2/profiles/SetBundles | Creates or updates bundle packages and associated profile mappings.
*CustomizationApi* | [**apiV2ProfilesSetConfigPost**](docs/Api/CustomizationApi.md#apiv2profilessetconfigpost) | **POST** /api/v2/profiles/SetConfig | Creates or updates configuration settings and associated profile mappings.
*CustomizationApi* | [**apiV2ProfilesSetExclusionsPost**](docs/Api/CustomizationApi.md#apiv2profilessetexclusionspost) | **POST** /api/v2/profiles/SetExclusions | Creates or updates exclusions and associated profile mappings.
*CustomizationApi* | [**apiV2ProfilesSetOverridesPost**](docs/Api/CustomizationApi.md#apiv2profilessetoverridespost) | **POST** /api/v2/profiles/SetOverrides | Creates or updates overrides and associated profile mappings.
*HealthCheckApi* | [**apiV2HealthCheckGet**](docs/Api/HealthCheckApi.md#apiv2healthcheckget) | **GET** /api/v2/HealthCheck | Health check that confirms the service is operational and ready to use
*JurisdictionDeterminationApi* | [**apiV2AfcPCodePost**](docs/Api/JurisdictionDeterminationApi.md#apiv2afcpcodepost) | **POST** /api/v2/afc/PCode | Get PCode(s) associated with a location - Ctry/State/County/City/Zip/NpaNxx/Fips.
*JurisdictionDeterminationApi* | [**apiV2GeoBatchLogProcessIdGet**](docs/Api/JurisdictionDeterminationApi.md#apiv2geobatchlogprocessidget) | **GET** /api/v2/geo/batch/log/{processId} | Retrieves log on Geo Batch file
*JurisdictionDeterminationApi* | [**apiV2GeoBatchStatusProcessIdGet**](docs/Api/JurisdictionDeterminationApi.md#apiv2geobatchstatusprocessidget) | **GET** /api/v2/geo/batch/status/{processId} | Retrieves information on Geo Batch file status
*JurisdictionDeterminationApi* | [**apiV2GeoBatchUploadPost**](docs/Api/JurisdictionDeterminationApi.md#apiv2geobatchuploadpost) | **POST** /api/v2/geo/batch/Upload | Uploads file to Geo Batch.
*JurisdictionDeterminationApi* | [**apiV2GeoGeocodePost**](docs/Api/JurisdictionDeterminationApi.md#apiv2geogeocodepost) | **POST** /api/v2/geo/Geocode | Geocodes one or multiple street addresses and/or lat/long coordinate pairs.
*LookupsApi* | [**apiV2AfcLocationPcodeGet**](docs/Api/LookupsApi.md#apiv2afclocationpcodeget) | **GET** /api/v2/afc/location/{pcode} | Get location data associated with a PCode
*LookupsApi* | [**apiV2AfcPrimaryPCodeGet**](docs/Api/LookupsApi.md#apiv2afcprimarypcodeget) | **GET** /api/v2/afc/primary/{pCode} | Get primary location data associated with a PCode
*LookupsApi* | [**apiV2AfcServiceinfoGet**](docs/Api/LookupsApi.md#apiv2afcserviceinfoget) | **GET** /api/v2/afc/serviceinfo | Retrieves server time, service build version and engine version
*LookupsApi* | [**apiV2AfcTaxtypeTaxTypeGet**](docs/Api/LookupsApi.md#apiv2afctaxtypetaxtypeget) | **GET** /api/v2/afc/taxtype/{taxType} | Get the tax information (description and category) for a tax type ID
*LookupsApi* | [**apiV2AfcTspairsGet**](docs/Api/LookupsApi.md#apiv2afctspairsget) | **GET** /api/v2/afc/tspairs | Get transaction/service pair information
*TaxCalculationApi* | [**apiV2AfcCalcTaxesPost**](docs/Api/TaxCalculationApi.md#apiv2afccalctaxespost) | **POST** /api/v2/afc/CalcTaxes | Performs tax calculations on all invoices and line items within the request body.
*TaxCalculationApi* | [**apiV2AfcCommitPost**](docs/Api/TaxCalculationApi.md#apiv2afccommitpost) | **POST** /api/v2/afc/Commit | Commits or un-commits a document code.


## Documentation For Models

 - [Address](docs/Model/Address.md)
 - [BillingPeriod](docs/Model/BillingPeriod.md)
 - [BundleConfig](docs/Model/BundleConfig.md)
 - [BundleItem](docs/Model/BundleItem.md)
 - [CalcTaxesRequest](docs/Model/CalcTaxesRequest.md)
 - [CalcTaxesResponse](docs/Model/CalcTaxesResponse.md)
 - [CommitRequest](docs/Model/CommitRequest.md)
 - [CommitResponse](docs/Model/CommitResponse.md)
 - [CompanyData](docs/Model/CompanyData.md)
 - [Configuration](docs/Model/Configuration.md)
 - [Error](docs/Model/Error.md)
 - [Exclusion](docs/Model/Exclusion.md)
 - [ExclusionConfig](docs/Model/ExclusionConfig.md)
 - [GeoBatchDownloadResponse](docs/Model/GeoBatchDownloadResponse.md)
 - [GeoBatchLog](docs/Model/GeoBatchLog.md)
 - [GeoBatchLogItem](docs/Model/GeoBatchLogItem.md)
 - [GeoBatchStatus](docs/Model/GeoBatchStatus.md)
 - [GeoBatchSubmitFileResponse](docs/Model/GeoBatchSubmitFileResponse.md)
 - [GeocodeRequest](docs/Model/GeocodeRequest.md)
 - [GeocodeResult](docs/Model/GeocodeResult.md)
 - [InlineObject](docs/Model/InlineObject.md)
 - [Invoice](docs/Model/Invoice.md)
 - [InvoiceResult](docs/Model/InvoiceResult.md)
 - [KeyValuePair](docs/Model/KeyValuePair.md)
 - [LineItem](docs/Model/LineItem.md)
 - [LineItemResult](docs/Model/LineItemResult.md)
 - [Location](docs/Model/Location.md)
 - [LocationItem](docs/Model/LocationItem.md)
 - [NexusConfig](docs/Model/NexusConfig.md)
 - [OverrideConfig](docs/Model/OverrideConfig.md)
 - [PCodeLookupRequest](docs/Model/PCodeLookupRequest.md)
 - [PCodeLookupResult](docs/Model/PCodeLookupResult.md)
 - [ReportingInformation](docs/Model/ReportingInformation.md)
 - [RequestConfig](docs/Model/RequestConfig.md)
 - [SafeHarborOverride](docs/Model/SafeHarborOverride.md)
 - [ServiceInfo](docs/Model/ServiceInfo.md)
 - [SetTaxCalculationSettingRequest](docs/Model/SetTaxCalculationSettingRequest.md)
 - [Status](docs/Model/Status.md)
 - [SummarizedTax](docs/Model/SummarizedTax.md)
 - [TSPairData](docs/Model/TSPairData.md)
 - [Tax](docs/Model/Tax.md)
 - [TaxBracket](docs/Model/TaxBracket.md)
 - [TaxCalculationSettingTypes](docs/Model/TaxCalculationSettingTypes.md)
 - [TaxCalculationSettingsResponse](docs/Model/TaxCalculationSettingsResponse.md)
 - [TaxExemption](docs/Model/TaxExemption.md)
 - [TaxOverride](docs/Model/TaxOverride.md)
 - [TaxTypeData](docs/Model/TaxTypeData.md)
 - [TrafficStudyOverride](docs/Model/TrafficStudyOverride.md)
 - [VersionInfo](docs/Model/VersionInfo.md)
 - [Warning](docs/Model/Warning.md)


## Documentation For Authorization



## Basic



## Author



