SCHEMA = {
  "typeName" : "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption",
  "description" : "Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ApplicationName" : {
      "type" : "string"
    },
    "CloudWatchLoggingOption" : {
      "$ref" : "#/definitions/CloudWatchLoggingOption"
    }
  },
  "definitions" : {
    "CloudWatchLoggingOption" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LogStreamARN" : {
          "type" : "string"
        }
      },
      "required" : [ "LogStreamARN" ]
    }
  },
  "required" : [ "CloudWatchLoggingOption", "ApplicationName" ],
  "createOnlyProperties" : [ "/properties/ApplicationName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}