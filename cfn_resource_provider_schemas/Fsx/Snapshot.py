SCHEMA = {
  "typeName" : "AWS::FSx::Snapshot",
  "description" : "Resource Type definition for AWS::FSx::Snapshot",
  "additionalProperties" : False,
  "properties" : {
    "ResourceARN" : {
      "type" : "string"
    },
    "VolumeId" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "VolumeId", "Name" ],
  "createOnlyProperties" : [ "/properties/VolumeId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/ResourceARN", "/properties/Id" ]
}