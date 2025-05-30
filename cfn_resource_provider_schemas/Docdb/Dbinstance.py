SCHEMA = {
  "typeName" : "AWS::DocDB::DBInstance",
  "description" : "Resource Type definition for AWS::DocDB::DBInstance",
  "additionalProperties" : False,
  "properties" : {
    "DBInstanceClass" : {
      "type" : "string"
    },
    "Port" : {
      "type" : "string"
    },
    "DBClusterIdentifier" : {
      "type" : "string"
    },
    "AvailabilityZone" : {
      "type" : "string"
    },
    "PreferredMaintenanceWindow" : {
      "type" : "string"
    },
    "EnablePerformanceInsights" : {
      "type" : "boolean"
    },
    "AutoMinorVersionUpgrade" : {
      "type" : "boolean"
    },
    "DBInstanceIdentifier" : {
      "type" : "string"
    },
    "CACertificateIdentifier" : {
      "type" : "string"
    },
    "CertificateRotationRestart" : {
      "type" : "boolean"
    },
    "Endpoint" : {
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
  "required" : [ "DBInstanceClass", "DBClusterIdentifier" ],
  "createOnlyProperties" : [ "/properties/DBClusterIdentifier", "/properties/AvailabilityZone", "/properties/DBInstanceIdentifier" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Port", "/properties/Id", "/properties/Endpoint" ]
}