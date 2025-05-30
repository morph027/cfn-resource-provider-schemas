SCHEMA = {
  "typeName" : "AWS::KinesisAnalyticsV2::ApplicationOutput",
  "description" : "Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationOutput",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ApplicationName" : {
      "type" : "string"
    },
    "Output" : {
      "$ref" : "#/definitions/Output"
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
    "KinesisStreamsOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN" ]
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
    "KinesisFirehoseOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN" ]
    },
    "LambdaOutput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceARN" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceARN" ]
    }
  },
  "required" : [ "ApplicationName", "Output" ],
  "createOnlyProperties" : [ "/properties/ApplicationName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}