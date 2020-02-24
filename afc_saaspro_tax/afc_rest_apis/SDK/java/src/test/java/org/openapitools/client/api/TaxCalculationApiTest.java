/*
 * SaasPro
 * APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.
 *
 * The version of the OpenAPI document: v2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CalcTaxesRequest;
import org.openapitools.client.model.CalcTaxesResponse;
import org.openapitools.client.model.CommitRequest;
import org.openapitools.client.model.CommitResponse;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TaxCalculationApi
 */
@Ignore
public class TaxCalculationApiTest {

    private final TaxCalculationApi api = new TaxCalculationApi();

    
    /**
     * Performs tax calculations on all invoices and line items within the request body.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiV2AfcCalcTaxesPostTest() throws ApiException {
        CalcTaxesRequest calcTaxesRequest = null;
        CalcTaxesResponse response = api.apiV2AfcCalcTaxesPost(calcTaxesRequest);

        // TODO: test validations
    }
    
    /**
     * Commits or un-commits a document code.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiV2AfcCommitPostTest() throws ApiException {
        CommitRequest commitRequest = null;
        CommitResponse response = api.apiV2AfcCommitPost(commitRequest);

        // TODO: test validations
    }
    
}