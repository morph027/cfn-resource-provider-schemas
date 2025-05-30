SCHEMA = {
  "typeName" : "AWS::Pinpoint::Campaign",
  "description" : "Resource Type definition for AWS::Pinpoint::Campaign",
  "additionalProperties" : False,
  "properties" : {
    "Description" : {
      "type" : "string"
    },
    "SegmentId" : {
      "type" : "string"
    },
    "Priority" : {
      "type" : "integer"
    },
    "TemplateConfiguration" : {
      "$ref" : "#/definitions/TemplateConfiguration"
    },
    "IsPaused" : {
      "type" : "boolean"
    },
    "AdditionalTreatments" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/WriteTreatmentResource"
      }
    },
    "Name" : {
      "type" : "string"
    },
    "SegmentVersion" : {
      "type" : "integer"
    },
    "TreatmentDescription" : {
      "type" : "string"
    },
    "MessageConfiguration" : {
      "$ref" : "#/definitions/MessageConfiguration"
    },
    "Limits" : {
      "$ref" : "#/definitions/Limits"
    },
    "CampaignId" : {
      "type" : "string"
    },
    "HoldoutPercent" : {
      "type" : "integer"
    },
    "Schedule" : {
      "$ref" : "#/definitions/Schedule"
    },
    "CustomDeliveryConfiguration" : {
      "$ref" : "#/definitions/CustomDeliveryConfiguration"
    },
    "Arn" : {
      "type" : "string"
    },
    "ApplicationId" : {
      "type" : "string"
    },
    "CampaignHook" : {
      "$ref" : "#/definitions/CampaignHook"
    },
    "Tags" : {
      "type" : "object"
    },
    "TreatmentName" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "QuietTime" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Start" : {
          "type" : "string"
        },
        "End" : {
          "type" : "string"
        }
      },
      "required" : [ "Start", "End" ]
    },
    "SetDimension" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Values" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DimensionType" : {
          "type" : "string"
        }
      }
    },
    "Message" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Action" : {
          "type" : "string"
        },
        "MediaUrl" : {
          "type" : "string"
        },
        "TimeToLive" : {
          "type" : "integer"
        },
        "ImageSmallIconUrl" : {
          "type" : "string"
        },
        "ImageUrl" : {
          "type" : "string"
        },
        "Title" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        },
        "JsonBody" : {
          "type" : "string"
        },
        "ImageIconUrl" : {
          "type" : "string"
        },
        "SilentPush" : {
          "type" : "boolean"
        },
        "Body" : {
          "type" : "string"
        },
        "RawContent" : {
          "type" : "string"
        }
      }
    },
    "InAppMessageContent" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BodyConfig" : {
          "$ref" : "#/definitions/InAppMessageBodyConfig"
        },
        "SecondaryBtn" : {
          "$ref" : "#/definitions/InAppMessageButton"
        },
        "ImageUrl" : {
          "type" : "string"
        },
        "PrimaryBtn" : {
          "$ref" : "#/definitions/InAppMessageButton"
        },
        "HeaderConfig" : {
          "$ref" : "#/definitions/InAppMessageHeaderConfig"
        },
        "BackgroundColor" : {
          "type" : "string"
        }
      }
    },
    "InAppMessageBodyConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Alignment" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        }
      }
    },
    "CampaignEventFilter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Dimensions" : {
          "$ref" : "#/definitions/EventDimensions"
        },
        "FilterType" : {
          "type" : "string"
        }
      }
    },
    "TemplateConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SMSTemplate" : {
          "$ref" : "#/definitions/Template"
        },
        "EmailTemplate" : {
          "$ref" : "#/definitions/Template"
        },
        "PushTemplate" : {
          "$ref" : "#/definitions/Template"
        },
        "VoiceTemplate" : {
          "$ref" : "#/definitions/Template"
        }
      }
    },
    "CampaignCustomMessage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Data" : {
          "type" : "string"
        }
      }
    },
    "EventDimensions" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Attributes" : {
          "type" : "object"
        },
        "Metrics" : {
          "type" : "object"
        },
        "EventType" : {
          "$ref" : "#/definitions/SetDimension"
        }
      }
    },
    "Template" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Version" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "MessageConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "APNSMessage" : {
          "$ref" : "#/definitions/Message"
        },
        "BaiduMessage" : {
          "$ref" : "#/definitions/Message"
        },
        "DefaultMessage" : {
          "$ref" : "#/definitions/Message"
        },
        "InAppMessage" : {
          "$ref" : "#/definitions/CampaignInAppMessage"
        },
        "EmailMessage" : {
          "$ref" : "#/definitions/CampaignEmailMessage"
        },
        "GCMMessage" : {
          "$ref" : "#/definitions/Message"
        },
        "SMSMessage" : {
          "$ref" : "#/definitions/CampaignSmsMessage"
        },
        "CustomMessage" : {
          "$ref" : "#/definitions/CampaignCustomMessage"
        },
        "ADMMessage" : {
          "$ref" : "#/definitions/Message"
        }
      }
    },
    "Limits" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MessagesPerSecond" : {
          "type" : "integer"
        },
        "Daily" : {
          "type" : "integer"
        },
        "MaximumDuration" : {
          "type" : "integer"
        },
        "Total" : {
          "type" : "integer"
        },
        "Session" : {
          "type" : "integer"
        }
      }
    },
    "WriteTreatmentResource" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TreatmentDescription" : {
          "type" : "string"
        },
        "MessageConfiguration" : {
          "$ref" : "#/definitions/MessageConfiguration"
        },
        "Schedule" : {
          "$ref" : "#/definitions/Schedule"
        },
        "TemplateConfiguration" : {
          "$ref" : "#/definitions/TemplateConfiguration"
        },
        "CustomDeliveryConfiguration" : {
          "$ref" : "#/definitions/CustomDeliveryConfiguration"
        },
        "SizePercent" : {
          "type" : "integer"
        },
        "TreatmentName" : {
          "type" : "string"
        }
      }
    },
    "CampaignInAppMessage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CustomConfig" : {
          "type" : "object"
        },
        "Layout" : {
          "type" : "string"
        },
        "Content" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/InAppMessageContent"
          }
        }
      }
    },
    "CampaignEmailMessage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Title" : {
          "type" : "string"
        },
        "FromAddress" : {
          "type" : "string"
        },
        "HtmlBody" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        }
      }
    },
    "CampaignSmsMessage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EntityId" : {
          "type" : "string"
        },
        "OriginationNumber" : {
          "type" : "string"
        },
        "SenderId" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        },
        "MessageType" : {
          "type" : "string"
        },
        "TemplateId" : {
          "type" : "string"
        }
      }
    },
    "Schedule" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimeZone" : {
          "type" : "string"
        },
        "QuietTime" : {
          "$ref" : "#/definitions/QuietTime"
        },
        "EndTime" : {
          "type" : "string"
        },
        "StartTime" : {
          "type" : "string"
        },
        "Frequency" : {
          "type" : "string"
        },
        "EventFilter" : {
          "$ref" : "#/definitions/CampaignEventFilter"
        },
        "IsLocalTime" : {
          "type" : "boolean"
        }
      }
    },
    "DefaultButtonConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ButtonAction" : {
          "type" : "string"
        },
        "BorderRadius" : {
          "type" : "integer"
        },
        "Text" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        },
        "Link" : {
          "type" : "string"
        },
        "BackgroundColor" : {
          "type" : "string"
        }
      }
    },
    "CustomDeliveryConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EndpointTypes" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DeliveryUri" : {
          "type" : "string"
        }
      }
    },
    "CampaignHook" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "WebUrl" : {
          "type" : "string"
        },
        "LambdaFunctionName" : {
          "type" : "string"
        },
        "Mode" : {
          "type" : "string"
        }
      }
    },
    "InAppMessageButton" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IOS" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        },
        "Web" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        },
        "DefaultConfig" : {
          "$ref" : "#/definitions/DefaultButtonConfiguration"
        },
        "Android" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        }
      }
    },
    "InAppMessageHeaderConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Alignment" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        },
        "Header" : {
          "type" : "string"
        }
      }
    },
    "OverrideButtonConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ButtonAction" : {
          "type" : "string"
        },
        "Link" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "SegmentId", "Schedule", "ApplicationId", "Name" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/CampaignId" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CampaignId" ]
}