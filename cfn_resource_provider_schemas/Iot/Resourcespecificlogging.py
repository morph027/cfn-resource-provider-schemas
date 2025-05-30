SCHEMA = {
  "typeName" : "AWS::IoT::ResourceSpecificLogging",
  "description" : "Resource-specific logging allows you to specify a logging level for a specific thing group.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "documentationUrl" : "https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html",
  "definitions" : { },
  "properties" : {
    "TargetType" : {
      "description" : "The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.",
      "type" : "string",
      "enum" : [ "THING_GROUP", "CLIENT_ID", "SOURCE_IP", "PRINCIPAL_ID", "EVENT_TYPE" ]
    },
    "TargetName" : {
      "description" : "The target name.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[a-zA-Z0-9.:\\s_\\-]+"
    },
    "LogLevel" : {
      "description" : "The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.",
      "type" : "string",
      "enum" : [ "ERROR", "WARN", "INFO", "DEBUG", "DISABLED" ]
    },
    "TargetId" : {
      "description" : "Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.",
      "type" : "string",
      "minLength" : 13,
      "maxLength" : 140,
      "pattern" : "[a-zA-Z0-9.:\\s_\\-]+"
    }
  },
  "createOnlyProperties" : [ "/properties/TargetName", "/properties/TargetType" ],
  "readOnlyProperties" : [ "/properties/TargetId" ],
  "additionalProperties" : False,
  "required" : [ "TargetName", "TargetType", "LogLevel" ],
  "taggable" : False,
  "primaryIdentifier" : [ "/properties/TargetId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:ListV2LoggingLevels", "iot:SetV2LoggingLevel" ]
    },
    "read" : {
      "permissions" : [ "iot:ListV2LoggingLevels" ]
    },
    "update" : {
      "permissions" : [ "iot:ListV2LoggingLevels", "iot:SetV2LoggingLevel" ]
    },
    "delete" : {
      "permissions" : [ "iot:ListV2LoggingLevels", "iot:DeleteV2LoggingLevel" ]
    },
    "list" : {
      "permissions" : [ "iot:ListV2LoggingLevels" ]
    }
  }
}