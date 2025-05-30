SCHEMA = {
  "typeName" : "AWS::ServiceDiscovery::Instance",
  "description" : "Resource Type definition for AWS::ServiceDiscovery::Instance",
  "additionalProperties" : False,
  "properties" : {
    "InstanceAttributes" : {
      "type" : "object"
    },
    "InstanceId" : {
      "type" : "string"
    },
    "ServiceId" : {
      "type" : "string"
    }
  },
  "required" : [ "InstanceAttributes", "ServiceId" ],
  "createOnlyProperties" : [ "/properties/InstanceId", "/properties/ServiceId" ],
  "primaryIdentifier" : [ "/properties/InstanceId" ],
  "readOnlyProperties" : [ "/properties/InstanceId" ]
}