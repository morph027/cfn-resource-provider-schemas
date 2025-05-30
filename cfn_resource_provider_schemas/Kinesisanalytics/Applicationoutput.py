SCHEMA = {
  "typeName" : "AWS::KinesisAnalytics::ApplicationOutput",
  "description" : "Resource Type definition for AWS::KinesisAnalytics::ApplicationOutput",
  "additionalProperties" : False,
  "properties" : {
    "ApplicationName" : {
      "type" : "string"
    },
    "Output" : {
      "$ref" : "#/definitions/Output"
    },
    "Id" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Output" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationSchema" : {
          "$ref" : "#/definitions/DestinationSchema"
        },
        "LambdaOutput" : {
          "$ref" : "#/definitions/LambdaOutput"
        },
        "KinesisFirehoseOutput" : {
          "$ref" : "#/definitions/KinesisFirehoseOutput"
        },
        "KinesisStreamsOutput" : {
          "$ref" : "#/definitions/KinesisStreamsOutput"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "DestinationSchema" ]
    },
    "DestinationSchema" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RecordFormatType" : {
          "type" : "string"
        }
      }
    },
    "LambdaOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        },
        "RoleARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN", "RoleARN" ]
    },
    "KinesisStreamsOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        },
        "RoleARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN", "RoleARN" ]
    },
    "KinesisFirehoseOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        },
        "RoleARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN", "RoleARN" ]
    }
  },
  "required" : [ "ApplicationName", "Output" ],
  "createOnlyProperties" : [ "/properties/ApplicationName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}