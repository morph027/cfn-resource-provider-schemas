SCHEMA = {
  "typeName" : "AWS::ConnectCampaigns::Campaign",
  "description" : "Definition of AWS::ConnectCampaigns::Campaign Resource Type",
  "definitions" : {
    "DialerConfig" : {
      "type" : "object",
      "description" : "The possible types of dialer config parameters",
      "properties" : {
        "ProgressiveDialerConfig" : {
          "$ref" : "#/definitions/ProgressiveDialerConfig"
        },
        "PredictiveDialerConfig" : {
          "$ref" : "#/definitions/PredictiveDialerConfig"
        },
        "AgentlessDialerConfig" : {
          "$ref" : "#/definitions/AgentlessDialerConfig"
        }
      },
      "additionalProperties" : False,
      "oneOf" : [ {
        "required" : [ "ProgressiveDialerConfig" ]
      }, {
        "required" : [ "PredictiveDialerConfig" ]
      }, {
        "required" : [ "AgentlessDialerConfig" ]
      } ]
    },
    "OutboundCallConfig" : {
      "type" : "object",
      "description" : "The configuration used for outbound calls.",
      "properties" : {
        "ConnectContactFlowArn" : {
          "type" : "string",
          "maxLength" : 500,
          "description" : "The identifier of the contact flow for the outbound call.",
          "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*$"
        },
        "ConnectSourcePhoneNumber" : {
          "type" : "string",
          "maxLength" : 100,
          "description" : "The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue."
        },
        "ConnectQueueArn" : {
          "type" : "string",
          "maxLength" : 500,
          "description" : "The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number.",
          "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/queue/[-a-zA-Z0-9]*$"
        },
        "AnswerMachineDetectionConfig" : {
          "$ref" : "#/definitions/AnswerMachineDetectionConfig"
        }
      },
      "required" : [ "ConnectContactFlowArn" ],
      "additionalProperties" : False
    },
    "PredictiveDialerConfig" : {
      "type" : "object",
      "description" : "Predictive Dialer config",
      "properties" : {
        "BandwidthAllocation" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0,
          "description" : "The bandwidth allocation of a queue resource."
        },
        "DialingCapacity" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0.01,
          "description" : "Allocates dialing capacity for this campaign between multiple active campaigns."
        }
      },
      "required" : [ "BandwidthAllocation" ],
      "additionalProperties" : False
    },
    "ProgressiveDialerConfig" : {
      "type" : "object",
      "description" : "Progressive Dialer config",
      "properties" : {
        "BandwidthAllocation" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0,
          "description" : "The bandwidth allocation of a queue resource."
        },
        "DialingCapacity" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0.01,
          "description" : "Allocates dialing capacity for this campaign between multiple active campaigns."
        }
      },
      "required" : [ "BandwidthAllocation" ],
      "additionalProperties" : False
    },
    "AgentlessDialerConfig" : {
      "type" : "object",
      "description" : "Agentless Dialer config",
      "properties" : {
        "DialingCapacity" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0.01,
          "description" : "Allocates dialing capacity for this campaign between multiple active campaigns."
        }
      },
      "required" : [ ],
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
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that's 1 to 256 characters in length.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "ConnectInstanceArn" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "description" : "Amazon Connect Instance Arn",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "DialerConfig" : {
      "$ref" : "#/definitions/DialerConfig"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "description" : "Amazon Connect Campaign Arn",
      "pattern" : "^arn:aws[-a-z0-9]*:connect-campaigns:[-a-z0-9]*:[0-9]{12}:campaign/[-a-zA-Z0-9]*$"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 127,
      "minLength" : 1,
      "description" : "Amazon Connect Campaign Name"
    },
    "OutboundCallConfig" : {
      "$ref" : "#/definitions/OutboundCallConfig"
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
  "required" : [ "ConnectInstanceArn", "DialerConfig", "Name", "OutboundCallConfig" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ConnectInstanceArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect-campaigns:CreateCampaign", "connect-campaigns:DescribeCampaign", "connect-campaigns:TagResource", "connect:DescribeContactFlow", "connect:DescribeInstance", "connect:DescribeQueue" ]
    },
    "read" : {
      "permissions" : [ "connect-campaigns:DescribeCampaign" ]
    },
    "delete" : {
      "permissions" : [ "connect-campaigns:DeleteCampaign" ]
    },
    "list" : {
      "permissions" : [ "connect-campaigns:ListCampaigns" ]
    },
    "update" : {
      "permissions" : [ "connect-campaigns:UpdateCampaignDialerConfig", "connect-campaigns:UpdateCampaignName", "connect-campaigns:UpdateCampaignOutboundCallConfig", "connect-campaigns:TagResource", "connect-campaigns:UntagResource", "connect-campaigns:DescribeCampaign" ]
    }
  },
  "additionalProperties" : False
}