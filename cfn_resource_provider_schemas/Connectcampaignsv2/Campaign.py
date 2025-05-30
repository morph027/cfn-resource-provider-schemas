SCHEMA = {
  "typeName" : "AWS::ConnectCampaignsV2::Campaign",
  "description" : "Definition of AWS::ConnectCampaignsV2::Campaign Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect-campaigns",
  "definitions" : {
    "CampaignName" : {
      "type" : "string",
      "maxLength" : 127,
      "minLength" : 1,
      "description" : "Campaign name"
    },
    "InstanceId" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "description" : "Amazon Connect Instance Id",
      "pattern" : "^[a-zA-Z0-9_\\-.]*$"
    },
    "Capacity" : {
      "type" : "number",
      "maximum" : 1,
      "minimum" : 0.01,
      "description" : "Allocates outbound capacity for the specific channel of this campaign between multiple active campaigns"
    },
    "QueueId" : {
      "type" : "string",
      "maxLength" : 500,
      "description" : "The queue for the call"
    },
    "ContactFlowId" : {
      "type" : "string",
      "maxLength" : 500,
      "description" : "The identifier of the contact flow for the outbound call"
    },
    "SourcePhoneNumber" : {
      "type" : "string",
      "maxLength" : 100,
      "description" : "The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue."
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 500,
      "minLength" : 20,
      "description" : "Arn",
      "pattern" : "^arn:.*$"
    },
    "EmailAddress" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "description" : "Email address used for Email messages",
      "pattern" : "^[\\w-\\.\\+]+@([\\w-]+\\.)+[\\w-]{2,4}$"
    },
    "SourceEmailAddressDisplayName" : {
      "type" : "string",
      "maxLength" : 127,
      "minLength" : 1,
      "description" : "The name of the source email address display name"
    },
    "BandwidthAllocation" : {
      "type" : "number",
      "maximum" : 1,
      "minimum" : 0,
      "description" : "The bandwidth allocation of a queue resource."
    },
    "TimeStamp" : {
      "type" : "string",
      "description" : "Timestamp with no UTC offset or timezone",
      "maxLength" : 100
    },
    "TimeZone" : {
      "type" : "string",
      "description" : "Time Zone Id in the IANA format"
    },
    "Iso8601Duration" : {
      "type" : "string",
      "description" : "Time duration in ISO 8601 format",
      "maxLength" : 50,
      "minLength" : 0,
      "pattern" : "^[a-zA-Z0-9.]*$"
    },
    "Iso8601Date" : {
      "type" : "string",
      "description" : "Date in ISO 8601 format, e.g. 2024-01-01",
      "pattern" : "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "Iso8601Time" : {
      "type" : "string",
      "description" : "Time in ISO 8601 format, e.g. T23:11",
      "pattern" : "^T\\d{2}:\\d{2}$"
    },
    "DayOfWeek" : {
      "type" : "string",
      "description" : "Day of week",
      "enum" : [ "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY" ]
    },
    "PredictiveConfig" : {
      "type" : "object",
      "description" : "Predictive config",
      "properties" : {
        "BandwidthAllocation" : {
          "$ref" : "#/definitions/BandwidthAllocation"
        }
      },
      "required" : [ "BandwidthAllocation" ],
      "additionalProperties" : False
    },
    "ProgressiveConfig" : {
      "type" : "object",
      "description" : "Progressive config",
      "properties" : {
        "BandwidthAllocation" : {
          "$ref" : "#/definitions/BandwidthAllocation"
        }
      },
      "required" : [ "BandwidthAllocation" ],
      "additionalProperties" : False
    },
    "AgentlessConfig" : {
      "type" : "object",
      "description" : "Agentless config",
      "required" : [ ],
      "additionalProperties" : False
    },
    "TelephonyOutboundMode" : {
      "type" : "object",
      "description" : "Telephony Outbound Mode",
      "properties" : {
        "ProgressiveConfig" : {
          "$ref" : "#/definitions/ProgressiveConfig"
        },
        "PredictiveConfig" : {
          "$ref" : "#/definitions/PredictiveConfig"
        },
        "AgentlessConfig" : {
          "$ref" : "#/definitions/AgentlessConfig"
        }
      },
      "oneOf" : [ {
        "required" : [ "ProgressiveConfig" ]
      }, {
        "required" : [ "PredictiveConfig" ]
      }, {
        "required" : [ "AgentlessConfig" ]
      } ],
      "additionalProperties" : False
    },
    "AnswerMachineDetectionConfig" : {
      "type" : "object",
      "description" : "The configuration used for answering machine detection during outbound calls",
      "properties" : {
        "EnableAnswerMachineDetection" : {
          "type" : "boolean",
          "description" : "Flag to decided whether outbound calls should have answering machine detection enabled or not"
        },
        "AwaitAnswerMachinePrompt" : {
          "type" : "boolean",
          "description" : "Enables detection of prompts (e.g., beep after after a voicemail greeting)"
        }
      },
      "required" : [ "EnableAnswerMachineDetection" ],
      "additionalProperties" : False
    },
    "TelephonyOutboundConfig" : {
      "type" : "object",
      "description" : "Default Telephone Outbound config",
      "properties" : {
        "ConnectContactFlowId" : {
          "$ref" : "#/definitions/ContactFlowId"
        },
        "ConnectSourcePhoneNumber" : {
          "$ref" : "#/definitions/SourcePhoneNumber"
        },
        "AnswerMachineDetectionConfig" : {
          "$ref" : "#/definitions/AnswerMachineDetectionConfig"
        }
      },
      "required" : [ "ConnectContactFlowId" ],
      "additionalProperties" : False
    },
    "TelephonyChannelSubtypeConfig" : {
      "type" : "object",
      "description" : "Telephony Channel Subtype config",
      "properties" : {
        "Capacity" : {
          "$ref" : "#/definitions/Capacity"
        },
        "ConnectQueueId" : {
          "$ref" : "#/definitions/QueueId"
        },
        "OutboundMode" : {
          "$ref" : "#/definitions/TelephonyOutboundMode"
        },
        "DefaultOutboundConfig" : {
          "$ref" : "#/definitions/TelephonyOutboundConfig"
        }
      },
      "required" : [ "OutboundMode", "DefaultOutboundConfig" ],
      "additionalProperties" : False
    },
    "SmsOutboundMode" : {
      "type" : "object",
      "description" : "SMS Outbound Mode",
      "properties" : {
        "AgentlessConfig" : {
          "$ref" : "#/definitions/AgentlessConfig"
        }
      },
      "additionalProperties" : False
    },
    "SmsOutboundConfig" : {
      "type" : "object",
      "description" : "Default SMS outbound config",
      "properties" : {
        "ConnectSourcePhoneNumberArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "WisdomTemplateArn" : {
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "ConnectSourcePhoneNumberArn", "WisdomTemplateArn" ],
      "additionalProperties" : False
    },
    "SmsChannelSubtypeConfig" : {
      "type" : "object",
      "description" : "SMS Channel Subtype config",
      "properties" : {
        "Capacity" : {
          "$ref" : "#/definitions/Capacity"
        },
        "OutboundMode" : {
          "$ref" : "#/definitions/SmsOutboundMode"
        },
        "DefaultOutboundConfig" : {
          "$ref" : "#/definitions/SmsOutboundConfig"
        }
      },
      "required" : [ "OutboundMode", "DefaultOutboundConfig" ],
      "additionalProperties" : False
    },
    "EmailOutboundMode" : {
      "type" : "object",
      "description" : "Email Outbound Mode",
      "properties" : {
        "AgentlessConfig" : {
          "$ref" : "#/definitions/AgentlessConfig"
        }
      },
      "additionalProperties" : False
    },
    "EmailOutboundConfig" : {
      "type" : "object",
      "description" : "Default SMS outbound config",
      "properties" : {
        "ConnectSourceEmailAddress" : {
          "$ref" : "#/definitions/EmailAddress"
        },
        "SourceEmailAddressDisplayName" : {
          "$ref" : "#/definitions/SourceEmailAddressDisplayName"
        },
        "WisdomTemplateArn" : {
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "ConnectSourceEmailAddress", "WisdomTemplateArn" ],
      "additionalProperties" : False
    },
    "EmailChannelSubtypeConfig" : {
      "type" : "object",
      "description" : "Email Channel Subtype config",
      "properties" : {
        "Capacity" : {
          "$ref" : "#/definitions/Capacity"
        },
        "OutboundMode" : {
          "$ref" : "#/definitions/EmailOutboundMode"
        },
        "DefaultOutboundConfig" : {
          "$ref" : "#/definitions/EmailOutboundConfig"
        }
      },
      "required" : [ "OutboundMode", "DefaultOutboundConfig" ],
      "additionalProperties" : False
    },
    "ChannelSubtypeConfig" : {
      "type" : "object",
      "description" : "The possible types of channel subtype config parameters",
      "properties" : {
        "Telephony" : {
          "$ref" : "#/definitions/TelephonyChannelSubtypeConfig"
        },
        "Sms" : {
          "$ref" : "#/definitions/SmsChannelSubtypeConfig"
        },
        "Email" : {
          "$ref" : "#/definitions/EmailChannelSubtypeConfig"
        }
      },
      "anyOf" : [ {
        "required" : [ "Telephony" ]
      }, {
        "required" : [ "Sms" ]
      }, {
        "required" : [ "Email" ]
      } ],
      "additionalProperties" : False
    },
    "Source" : {
      "type" : "object",
      "description" : "The possible source of the campaign",
      "properties" : {
        "CustomerProfilesSegmentArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "EventTrigger" : {
          "$ref" : "#/definitions/EventTrigger"
        }
      },
      "oneOf" : [ {
        "required" : [ "CustomerProfilesSegmentArn" ]
      }, {
        "required" : [ "EventTrigger" ]
      } ],
      "additionalProperties" : False
    },
    "EventTrigger" : {
      "type" : "object",
      "description" : "The event trigger of the campaign",
      "properties" : {
        "CustomerProfilesDomainArn" : {
          "$ref" : "#/definitions/Arn"
        }
      },
      "additionalProperties" : False
    },
    "TimeRange" : {
      "type" : "object",
      "description" : "Time range in 24 hour format",
      "properties" : {
        "StartTime" : {
          "$ref" : "#/definitions/Iso8601Time"
        },
        "EndTime" : {
          "$ref" : "#/definitions/Iso8601Time"
        }
      },
      "required" : [ "StartTime", "EndTime" ],
      "additionalProperties" : False
    },
    "TimeRangeList" : {
      "type" : "array",
      "description" : "List of time range",
      "items" : {
        "$ref" : "#/definitions/TimeRange"
      },
      "insertionOrder" : False
    },
    "DailyHour" : {
      "type" : "object",
      "description" : "Daily Hour",
      "properties" : {
        "Key" : {
          "$ref" : "#/definitions/DayOfWeek"
        },
        "Value" : {
          "$ref" : "#/definitions/TimeRangeList"
        }
      },
      "additionalProperties" : False
    },
    "DailyHours" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "Daily Hours map",
      "items" : {
        "$ref" : "#/definitions/DailyHour"
      }
    },
    "OpenHours" : {
      "type" : "object",
      "description" : "Open Hours config",
      "properties" : {
        "DailyHours" : {
          "$ref" : "#/definitions/DailyHours"
        }
      },
      "required" : [ "DailyHours" ],
      "additionalProperties" : False
    },
    "RestrictedPeriod" : {
      "type" : "object",
      "description" : "Restricted period",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 127,
          "description" : "The name of a restricted period"
        },
        "StartDate" : {
          "$ref" : "#/definitions/Iso8601Date"
        },
        "EndDate" : {
          "$ref" : "#/definitions/Iso8601Date"
        }
      },
      "required" : [ "StartDate", "EndDate" ],
      "additionalProperties" : False
    },
    "RestrictedPeriodList" : {
      "type" : "array",
      "description" : "List of restricted period",
      "items" : {
        "$ref" : "#/definitions/RestrictedPeriod"
      },
      "insertionOrder" : False
    },
    "RestrictedPeriods" : {
      "type" : "object",
      "description" : "Restricted period config",
      "properties" : {
        "RestrictedPeriodList" : {
          "$ref" : "#/definitions/RestrictedPeriodList"
        }
      },
      "oneOf" : [ {
        "required" : [ "RestrictedPeriodList" ]
      } ],
      "additionalProperties" : False
    },
    "TimeWindow" : {
      "type" : "object",
      "description" : "Time window config",
      "properties" : {
        "OpenHours" : {
          "$ref" : "#/definitions/OpenHours"
        },
        "RestrictedPeriods" : {
          "$ref" : "#/definitions/RestrictedPeriods"
        }
      },
      "required" : [ "OpenHours" ],
      "additionalProperties" : False
    },
    "Schedule" : {
      "type" : "object",
      "description" : "Campaign schedule",
      "properties" : {
        "StartTime" : {
          "$ref" : "#/definitions/TimeStamp"
        },
        "EndTime" : {
          "$ref" : "#/definitions/TimeStamp"
        },
        "RefreshFrequency" : {
          "$ref" : "#/definitions/Iso8601Duration"
        }
      },
      "required" : [ "StartTime", "EndTime" ],
      "additionalProperties" : False
    },
    "LocalTimeZoneDetectionType" : {
      "type" : "string",
      "description" : "Local TimeZone Detection method",
      "enum" : [ "ZIP_CODE", "AREA_CODE" ]
    },
    "LocalTimeZoneDetection" : {
      "type" : "array",
      "description" : "Local TimeZone Detection method list",
      "items" : {
        "$ref" : "#/definitions/LocalTimeZoneDetectionType"
      },
      "insertionOrder" : False
    },
    "LocalTimeZoneConfig" : {
      "type" : "object",
      "description" : "Local time zone config",
      "properties" : {
        "DefaultTimeZone" : {
          "$ref" : "#/definitions/TimeZone"
        },
        "LocalTimeZoneDetection" : {
          "$ref" : "#/definitions/LocalTimeZoneDetection"
        }
      },
      "additionalProperties" : False
    },
    "CommunicationTimeConfig" : {
      "type" : "object",
      "description" : "Campaign communication time config",
      "properties" : {
        "LocalTimeZoneConfig" : {
          "$ref" : "#/definitions/LocalTimeZoneConfig"
        },
        "Telephony" : {
          "$ref" : "#/definitions/TimeWindow"
        },
        "Sms" : {
          "$ref" : "#/definitions/TimeWindow"
        },
        "Email" : {
          "$ref" : "#/definitions/TimeWindow"
        }
      },
      "required" : [ "LocalTimeZoneConfig" ],
      "additionalProperties" : False
    },
    "CommunicationLimitTimeUnit" : {
      "type" : "string",
      "description" : "The communication limit time unit",
      "enum" : [ "DAY" ]
    },
    "CommunicationLimit" : {
      "type" : "object",
      "description" : "Communication Limit",
      "properties" : {
        "MaxCountPerRecipient" : {
          "type" : "integer",
          "minimum" : 1
        },
        "Frequency" : {
          "type" : "integer",
          "minimum" : 1
        },
        "Unit" : {
          "$ref" : "#/definitions/CommunicationLimitTimeUnit"
        }
      },
      "required" : [ "MaxCountPerRecipient", "Frequency", "Unit" ],
      "additionalProperties" : False
    },
    "CommunicationLimitList" : {
      "type" : "array",
      "description" : "List of communication limit",
      "items" : {
        "$ref" : "#/definitions/CommunicationLimit"
      },
      "insertionOrder" : False
    },
    "CommunicationLimits" : {
      "type" : "object",
      "description" : "Communication limits",
      "properties" : {
        "CommunicationLimitList" : {
          "$ref" : "#/definitions/CommunicationLimitList"
        }
      },
      "additionalProperties" : False
    },
    "CommunicationLimitsConfig" : {
      "type" : "object",
      "description" : "Communication limits config",
      "properties" : {
        "AllChannelsSubtypes" : {
          "$ref" : "#/definitions/CommunicationLimits"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag."
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "description" : "Amazon Connect Campaign Arn",
      "pattern" : "^arn:aws[-a-z0-9]*:connect-campaigns:[-a-z0-9]*:[0-9]{12}:campaign/[-a-zA-Z0-9]*$"
    },
    "Name" : {
      "$ref" : "#/definitions/CampaignName"
    },
    "ConnectInstanceId" : {
      "$ref" : "#/definitions/InstanceId"
    },
    "ChannelSubtypeConfig" : {
      "$ref" : "#/definitions/ChannelSubtypeConfig"
    },
    "Source" : {
      "$ref" : "#/definitions/Source"
    },
    "ConnectCampaignFlowArn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Schedule" : {
      "$ref" : "#/definitions/Schedule"
    },
    "CommunicationTimeConfig" : {
      "$ref" : "#/definitions/CommunicationTimeConfig"
    },
    "CommunicationLimitsOverride" : {
      "$ref" : "#/definitions/CommunicationLimitsConfig"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "One or more tags.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "connect-campaigns:UntagResource", "connect-campaigns:TagResource" ]
  },
  "required" : [ "Name", "ConnectInstanceId", "ChannelSubtypeConfig" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ConnectInstanceId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect-campaigns:CreateCampaign", "connect-campaigns:DescribeCampaign", "connect-campaigns:TagResource", "connect:DescribeContactFlow", "connect:DescribeEmailAddress", "connect:DescribeInstance", "connect:DescribePhoneNumber", "connect:DescribeQueue", "profile:GetSegmentDefinition", "wisdom:GetMessageTemplate" ]
    },
    "read" : {
      "permissions" : [ "connect-campaigns:DescribeCampaign" ]
    },
    "delete" : {
      "permissions" : [ "connect-campaigns:DeleteCampaign", "connect-campaigns:DeleteCampaignChannelSubtypeConfig", "connect-campaigns:DeleteCampaignCommunicationLimits", "connect-campaigns:DeleteCampaignCommunicationTime" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ConnectInstanceId" : {
            "$ref" : "resource-schema.json#/properties/ConnectInstanceId"
          }
        },
        "required" : [ "ConnectInstanceId" ]
      },
      "permissions" : [ "connect-campaigns:ListCampaigns" ]
    },
    "update" : {
      "permissions" : [ "connect-campaigns:DeleteCampaignChannelSubtypeConfig", "connect-campaigns:DeleteCampaignCommunicationLimits", "connect-campaigns:DeleteCampaignCommunicationTime", "connect-campaigns:UpdateCampaignChannelSubtypeConfig", "connect-campaigns:UpdateCampaignCommunicationLimits", "connect-campaigns:UpdateCampaignCommunicationTime", "connect-campaigns:UpdateCampaignName", "connect-campaigns:UpdateCampaignFlowAssociation", "connect-campaigns:UpdateCampaignSchedule", "connect-campaigns:UpdateCampaignSource", "connect-campaigns:TagResource", "connect-campaigns:UntagResource", "connect-campaigns:DescribeCampaign", "connect:DescribeContactFlow", "connect:DescribeEmailAddress", "connect:DescribePhoneNumber", "connect:DescribeQueue", "profile:GetSegmentDefinition", "wisdom:GetMessageTemplate" ]
    }
  },
  "additionalProperties" : False
}