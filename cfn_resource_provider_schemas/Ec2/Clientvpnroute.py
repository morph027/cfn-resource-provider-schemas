SCHEMA = {
  "typeName" : "AWS::EC2::ClientVpnRoute",
  "description" : "Resource Type definition for AWS::EC2::ClientVpnRoute",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ClientVpnEndpointId" : {
      "type" : "string"
    },
    "TargetVpcSubnetId" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "DestinationCidrBlock" : {
      "type" : "string"
    }
  },
  "required" : [ "ClientVpnEndpointId", "TargetVpcSubnetId", "DestinationCidrBlock" ],
  "createOnlyProperties" : [ "/properties/ClientVpnEndpointId", "/properties/DestinationCidrBlock", "/properties/Description", "/properties/TargetVpcSubnetId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}