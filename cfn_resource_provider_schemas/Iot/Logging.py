SCHEMA = {
  "typeName" : "AWS::IoT::Logging",
  "description" : "Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "documentationUrl" : "https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html",
  "definitions" : { },
  "properties" : {
    "AccountId" : {
      "description" : "Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).",
      "type" : "string",
      "minLength" : 12,
      "maxLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "RoleArn" : {
      "description" : "The ARN of the role that allows IoT to write to Cloudwatch logs.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "DefaultLogLevel" : {
      "description" : "The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.",
      "type" : "string",
      "enum" : [ "ERROR", "WARN", "INFO", "DEBUG", "DISABLED" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "AccountId", "RoleArn", "DefaultLogLevel" ],
  "taggable" : False,
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "createOnlyProperties" : [ "/properties/AccountId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:SetV2LoggingOptions", "iot:GetV2LoggingOptions", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "iot:GetV2LoggingOptions" ]
    },
    "update" : {
      "permissions" : [ "iot:SetV2LoggingOptions", "iot:GetV2LoggingOptions", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "iot:SetV2LoggingOptions", "iot:GetV2LoggingOptions" ]
    },
    "list" : {
      "permissions" : [ "iot:GetV2LoggingOptions" ]
    }
  }
}