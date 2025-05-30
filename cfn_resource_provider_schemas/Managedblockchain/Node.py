SCHEMA = {
  "typeName" : "AWS::ManagedBlockchain::Node",
  "description" : "Resource Type definition for AWS::ManagedBlockchain::Node",
  "additionalProperties" : False,
  "properties" : {
    "NodeId" : {
      "type" : "string"
    },
    "MemberId" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "NetworkId" : {
      "type" : "string"
    },
    "NodeConfiguration" : {
      "$ref" : "#/definitions/NodeConfiguration"
    }
  },
  "definitions" : {
    "NodeConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InstanceType" : {
          "type" : "string"
        },
        "AvailabilityZone" : {
          "type" : "string"
        }
      },
      "required" : [ "AvailabilityZone", "InstanceType" ]
    }
  },
  "required" : [ "MemberId", "NetworkId", "NodeConfiguration" ],
  "primaryIdentifier" : [ "/properties/NodeId" ],
  "readOnlyProperties" : [ "/properties/NodeId", "/properties/Arn" ]
}