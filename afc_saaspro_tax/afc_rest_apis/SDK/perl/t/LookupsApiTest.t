=begin comment

SaasPro

APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.

The version of the OpenAPI document: v2

Generated by: https://openapi-generator.tech

=end comment

=cut

#
# NOTE: This class is auto generated by OpenAPI Generator
# Please update the test cases below to test the API endpoints.
# Ref: https://openapi-generator.tech
#
use Test::More tests => 1; #TODO update number of test cases
use Test::Exception;

use lib 'lib';
use strict;
use warnings;

use_ok('WWW::OpenAPIClient::LookupsApi');

my $api = WWW::OpenAPIClient::LookupsApi->new();
isa_ok($api, 'WWW::OpenAPIClient::LookupsApi');

#
# api_v2_afc_location_pcode_get test
#
{
    my $pcode = undef; # replace NULL with a proper value
    my $result = $api->api_v2_afc_location_pcode_get(pcode => $pcode);
}

#
# api_v2_afc_primary_p_code_get test
#
{
    my $p_code = undef; # replace NULL with a proper value
    my $result = $api->api_v2_afc_primary_p_code_get(p_code => $p_code);
}

#
# api_v2_afc_serviceinfo_get test
#
{
    my $result = $api->api_v2_afc_serviceinfo_get();
}

#
# api_v2_afc_taxtype_tax_type_get test
#
{
    my $tax_type = undef; # replace NULL with a proper value
    my $result = $api->api_v2_afc_taxtype_tax_type_get(tax_type => $tax_type);
}

#
# api_v2_afc_tspairs_get test
#
{
    my $result = $api->api_v2_afc_tspairs_get();
}


1;
