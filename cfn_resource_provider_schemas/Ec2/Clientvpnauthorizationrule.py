SCHEMA = {
  "typeName" : "AWS::EC2::ClientVpnAuthorizationRule",
  "description" : "Resource Type definition for AWS::EC2::ClientVpnAuthorizationRule",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ClientVpnEndpointId" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "AccessGroupId" : {
      "type" : "string"
    },
    "TargetNetworkCidr" : {
      "type" : "string"
    },
    "AuthorizeAllGroups" : {
      "type" : "boolean"
    }
  },
  "required" : [ "ClientVpnEndpointId", "TargetNetworkCidr" ],
  "createOnlyProperties" : [ "/properties/ClientVpnEndpointId", "/properties/AuthorizeAllGroups", "/properties/Description", "/properties/AccessGroupId", "/properties/TargetNetworkCidr" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}