# WWW::OpenAPIClient::Object::LineItem

## Load the model package
```perl
use WWW::OpenAPIClient::Object::LineItem;
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **string** |  | [optional] 
**from** | [**Location**](Location.md) | Location for origination point. If null, will default to Invoice&#39;s BillTo location. | [optional] 
**to** | [**Location**](Location.md) | Location for destination point. If null, will default to Invoice&#39;s BillTo location. | [optional] 
**chg** | **double** |  | [optional] 
**line** | **int** |  | [optional] 
**loc** | **int** |  | [optional] 
**min** | **double** |  | [optional] 
**sale** | **int** |  | [optional] 
**plsp** | **double** |  | [optional] 
**incl** | **boolean** |  | [optional] 
**pror** | **double** |  | [optional] 
**proadj** | **int** |  | [optional] 
**tran** | **int** |  | [optional] 
**serv** | **int** |  | [optional] 
**dbt** | **boolean** |  | [optional] 
**adj** | **boolean** |  | [optional] 
**adjm** | **int** |  | [optional] 
**disc** | **int** |  | [optional] 
**opt** | [**ARRAY[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**prop** | **int** |  | [optional] 
**bill** | [**Location**](Location.md) |  | [optional] 
**cust** | **int** |  | [optional] 
**lfln** | **boolean** |  | [optional] 
**date** | **DateTime** | Invoice date. | [optional] 
**qty** | **int** |  | [optional] 
**glref** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

