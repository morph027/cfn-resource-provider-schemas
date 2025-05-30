SCHEMA = {
  "typeName" : "AWS::Lex::BotAlias",
  "description" : "A Bot Alias enables you to change the version of a bot without updating applications that use the bot",
  "sourceUrl" : "https://docs.aws.amazon.com/lexv2/latest/dg/API_CreateBotAlias.html",
  "definitions" : {
    "LocaleId" : {
      "description" : "The identifier of the language and locale that the bot alias will be configured in.",
      "type" : "string"
    },
    "BotAliasLocaleSettingsList" : {
      "description" : "A list of bot alias locale settings to add to the bot alias.",
      "type" : "array",
      "uniqueItems" : True,
      "maxItems" : 50,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/BotAliasLocaleSettingsItem"
      }
    },
    "BotAliasStatus" : {
      "type" : "string",
      "enum" : [ "Creating", "Available", "Deleting", "Failed" ]
    },
    "BotAliasLocaleSettingsItem" : {
      "description" : "A locale setting in alias",
      "type" : "object",
      "properties" : {
        "LocaleId" : {
          "description" : "A string used to identify the locale",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "BotAliasLocaleSetting" : {
          "$ref" : "#/definitions/BotAliasLocaleSettings"
        }
      },
      "required" : [ "LocaleId", "BotAliasLocaleSetting" ],
      "additionalProperties" : False
    },
    "BotAliasLocaleSettings" : {
      "description" : "You can use this parameter to specify a specific Lambda function to run different functions in different locales.",
      "type" : "object",
      "properties" : {
        "CodeHookSpecification" : {
          "$ref" : "#/definitions/CodeHookSpecification"
        },
        "Enabled" : {
          "type" : "boolean",
          "description" : "Whether the Lambda code hook is enabled"
        }
      },
      "required" : [ "Enabled" ],
      "additionalProperties" : False
    },
    "CodeHookSpecification" : {
      "description" : "Contains information about code hooks that Amazon Lex calls during a conversation.",
      "type" : "object",
      "properties" : {
        "LambdaCodeHook" : {
          "$ref" : "#/definitions/LambdaCodeHook"
        }
      },
      "required" : [ "LambdaCodeHook" ],
      "additionalProperties" : False
    },
    "LambdaCodeHook" : {
      "description" : "Contains information about code hooks that Amazon Lex calls during a conversation.",
      "type" : "object",
      "properties" : {
        "CodeHookInterfaceVersion" : {
          "description" : "The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 5
        },
        "LambdaArn" : {
          "description" : "The Amazon Resource Name (ARN) of the Lambda function.",
          "type" : "string",
          "minLength" : 20,
          "maxLength" : 2048
        }
      },
      "required" : [ "CodeHookInterfaceVersion", "LambdaArn" ],
      "additionalProperties" : False
    },
    "ConversationLogSettings" : {
      "description" : "Contains information about code hooks that Amazon Lex calls during a conversation.",
      "type" : "object",
      "properties" : {
        "AudioLogSettings" : {
          "$ref" : "#/definitions/AudioLogSettings"
        },
        "TextLogSettings" : {
          "$ref" : "#/definitions/TextLogSettings"
        }
      },
      "additionalProperties" : False
    },
    "AudioLogSettings" : {
      "description" : "List of audio log settings",
      "type" : "array",
      "maxItems" : 1,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/AudioLogSetting"
      }
    },
    "TextLogSettings" : {
      "description" : "List of text log settings",
      "type" : "array",
      "maxItems" : 1,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TextLogSetting"
      }
    },
    "AudioLogSetting" : {
      "description" : "Settings for logging audio of conversations between Amazon Lex and a user. You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.",
      "type" : "object",
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/AudioLogDestination"
        },
        "Enabled" : {
          "type" : "boolean",
          "description" : ""
        }
      },
      "required" : [ "Destination", "Enabled" ],
      "additionalProperties" : False
    },
    "TextLogSetting" : {
      "description" : "Contains information about code hooks that Amazon Lex calls during a conversation.",
      "type" : "object",
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/TextLogDestination"
        },
        "Enabled" : {
          "type" : "boolean",
          "description" : ""
        }
      },
      "required" : [ "Destination", "Enabled" ],
      "additionalProperties" : False
    },
    "AudioLogDestination" : {
      "description" : "The location of audio log files collected when conversation logging is enabled for a bot.",
      "type" : "object",
      "properties" : {
        "S3Bucket" : {
          "$ref" : "#/definitions/S3BucketLogDestination"
        }
      },
      "required" : [ "S3Bucket" ],
      "additionalProperties" : False
    },
    "TextLogDestination" : {
      "description" : "Defines the Amazon CloudWatch Logs destination log group for conversation text logs.",
      "type" : "object",
      "properties" : {
        "CloudWatch" : {
          "$ref" : "#/definitions/CloudWatchLogGroupLogDestination"
        }
      },
      "required" : [ "CloudWatch" ],
      "additionalProperties" : False
    },
    "CloudWatchLogGroupLogDestination" : {
      "type" : "object",
      "properties" : {
        "CloudWatchLogGroupArn" : {
          "description" : "A string used to identify the groupArn for the Cloudwatch Log Group",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "LogPrefix" : {
          "description" : "A string containing the value for the Log Prefix",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        }
      },
      "required" : [ "CloudWatchLogGroupArn", "LogPrefix" ],
      "additionalProperties" : False
    },
    "S3BucketLogDestination" : {
      "description" : "Specifies an Amazon S3 bucket for logging audio conversations",
      "type" : "object",
      "properties" : {
        "S3BucketArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "^arn:[\\w\\-]+:s3:::[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$"
        },
        "LogPrefix" : {
          "type" : "string",
          "description" : "The Amazon S3 key of the deployment package.",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "KmsKeyArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.",
          "minLength" : 20,
          "maxLength" : 2048,
          "pattern" : "^arn:[\\w\\-]+:kms:[\\w\\-]+:[\\d]{12}:(?:key\\/[\\w\\-]+|alias\\/[a-zA-Z0-9:\\/_\\-]{1,256})$"
        }
      },
      "required" : [ "LogPrefix", "S3BucketArn" ],
      "additionalProperties" : False
    },
    "Id" : {
      "description" : "Unique ID of resource",
      "type" : "string",
      "minLength" : 10,
      "maxLength" : 10,
      "pattern" : "^[0-9a-zA-Z]+$"
    },
    "Name" : {
      "description" : "A unique identifier for a resource.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100,
      "pattern" : "^([0-9a-zA-Z][_-]?)+$"
    },
    "BotVersion" : {
      "description" : "The version of a bot.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 5,
      "pattern" : "^(DRAFT|[0-9]+)$"
    },
    "Description" : {
      "description" : "A description of the bot alias. Use the description to help identify the bot alias in lists.",
      "type" : "string",
      "maxLength" : 200
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 1000
    },
    "Tag" : {
      "description" : "A label for tagging Lex resources",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A string used to identify this tag",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "BotAliasId" : {
      "$ref" : "#/definitions/Id"
    },
    "BotId" : {
      "$ref" : "#/definitions/Id"
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "BotAliasStatus" : {
      "$ref" : "#/definitions/BotAliasStatus"
    },
    "BotAliasLocaleSettings" : {
      "$ref" : "#/definitions/BotAliasLocaleSettingsList"
    },
    "BotAliasName" : {
      "$ref" : "#/definitions/Name"
    },
    "BotVersion" : {
      "$ref" : "#/definitions/BotVersion"
    },
    "ConversationLogSettings" : {
      "$ref" : "#/definitions/ConversationLogSettings"
    },
    "Description" : {
      "$ref" : "#/definitions/Description"
    },
    "SentimentAnalysisSettings" : {
      "description" : "Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.",
      "type" : "object",
      "properties" : {
        "DetectSentiment" : {
          "type" : "boolean",
          "description" : "Enable to call Amazon Comprehend for Sentiment natively within Lex"
        }
      },
      "required" : [ "DetectSentiment" ],
      "additionalProperties" : False
    },
    "BotAliasTags" : {
      "description" : "A list of tags to add to the bot alias.",
      "type" : "array",
      "uniqueItems" : True,
      "maxItems" : 200,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "taggable" : False,
  "additionalProperties" : False,
  "required" : [ "BotId", "BotAliasName" ],
  "readOnlyProperties" : [ "/properties/BotAliasId", "/properties/Arn", "/properties/BotAliasStatus" ],
  "primaryIdentifier" : [ "/properties/BotAliasId", "/properties/BotId" ],
  "createOnlyProperties" : [ "/properties/BotId" ],
  "writeOnlyProperties" : [ "/properties/BotAliasTags" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lex:CreateBotAlias", "lex:DescribeBot" ]
    },
    "update" : {
      "permissions" : [ "lex:UpdateBotAlias", "lex:DescribeBotAlias", "lex:ListTagsForResource", "lex:TagResource", "lex:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lex:DescribeBotAlias" ]
    },
    "delete" : {
      "permissions" : [ "lex:DeleteBotAlias" ]
    },
    "list" : {
      "permissions" : [ "lex:ListBotAliases" ]
    }
  }
}