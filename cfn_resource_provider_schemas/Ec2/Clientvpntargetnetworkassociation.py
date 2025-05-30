SCHEMA = {
  "typeName" : "AWS::EC2::ClientVpnTargetNetworkAssociation",
  "description" : "Resource Type definition for AWS::EC2::ClientVpnTargetNetworkAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ClientVpnEndpointId" : {
      "type" : "string"
    },
    "SubnetId" : {
      "type" : "string"
    }
  },
  "required" : [ "ClientVpnEndpointId", "SubnetId" ],
  "createOnlyProperties" : [ "/properties/ClientVpnEndpointId", "/properties/SubnetId" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}