SCHEMA = {
  "typeName" : "AWS::EC2::NetworkInterfacePermission",
  "description" : "Resource Type definition for AWS::EC2::NetworkInterfacePermission",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "AwsAccountId" : {
      "type" : "string"
    },
    "NetworkInterfaceId" : {
      "type" : "string"
    },
    "Permission" : {
      "type" : "string"
    }
  },
  "required" : [ "AwsAccountId", "NetworkInterfaceId", "Permission" ],
  "createOnlyProperties" : [ "/properties/AwsAccountId", "/properties/Permission", "/properties/NetworkInterfaceId" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}