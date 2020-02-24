/* 
 * SaasPro
 *
 * APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.
 *
 * The version of the OpenAPI document: v2
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using Xunit;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using avalara.comms.rest.v2.Api;
using avalara.comms.rest.v2.Model;
using avalara.comms.rest.v2.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace avalara.comms.rest.v2.Test
{
    /// <summary>
    ///  Class for testing TaxOverride
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class TaxOverrideTests : IDisposable
    {
        // TODO uncomment below to declare an instance variable for TaxOverride
        //private TaxOverride instance;

        public TaxOverrideTests()
        {
            // TODO uncomment below to create an instance of TaxOverride
            //instance = new TaxOverride();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of TaxOverride
        /// </summary>
        [Fact]
        public void TaxOverrideInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOfType" TaxOverride
            //Assert.IsInstanceOfType<TaxOverride> (instance, "variable 'instance' is a TaxOverride");
        }


        /// <summary>
        /// Test the property 'Loc'
        /// </summary>
        [Fact]
        public void LocTest()
        {
            // TODO unit test for the property 'Loc'
        }
        /// <summary>
        /// Test the property 'Scp'
        /// </summary>
        [Fact]
        public void ScpTest()
        {
            // TODO unit test for the property 'Scp'
        }
        /// <summary>
        /// Test the property 'Tid'
        /// </summary>
        [Fact]
        public void TidTest()
        {
            // TODO unit test for the property 'Tid'
        }
        /// <summary>
        /// Test the property 'Lvl'
        /// </summary>
        [Fact]
        public void LvlTest()
        {
            // TODO unit test for the property 'Lvl'
        }
        /// <summary>
        /// Test the property 'LvlExm'
        /// </summary>
        [Fact]
        public void LvlExmTest()
        {
            // TODO unit test for the property 'LvlExm'
        }
        /// <summary>
        /// Test the property 'Brkt'
        /// </summary>
        [Fact]
        public void BrktTest()
        {
            // TODO unit test for the property 'Brkt'
        }

    }

}