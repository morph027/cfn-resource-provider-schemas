SCHEMA = {
  "typeName" : "AWS::SecurityHub::Standard",
  "description" : "The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation.\n You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.\n For more information about ASH standards, see [standards reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) in the *User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "definitions" : {
    "StandardsControl" : {
      "description" : "Provides details about an individual security control. For a list of ASH controls, see [controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html) in the *User Guide*.",
      "type" : "object",
      "properties" : {
        "StandardsControlArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) of the control.",
          "pattern" : "arn:aws\\S*:securityhub:\\S*"
        },
        "Reason" : {
          "type" : "string",
          "description" : "A user-defined reason for changing a control's enablement status in a specified standard. If you are disabling a control, then this property is required."
        }
      },
      "required" : [ "StandardsControlArn" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "StandardsSubscriptionArn" : {
      "description" : "",
      "type" : "string",
      "pattern" : "arn:aws\\S*:securityhub:\\S*"
    },
    "StandardsArn" : {
      "description" : "The ARN of the standard that you want to enable. To view a list of available ASH standards and their ARNs, use the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation.",
      "type" : "string",
      "pattern" : "arn:aws\\S*:securityhub:\\S"
    },
    "DisabledStandardsControls" : {
      "description" : "Specifies which controls are to be disabled in a standard. \n *Maximum*: ``100``",
      "type" : "array",
      "minItems" : 0,
      "maxItems" : 100,
      "items" : {
        "$ref" : "#/definitions/StandardsControl"
      },
      "insertionOrder" : True,
      "uniqueItems" : True
    }
  },
  "additionalProperties" : False,
  "required" : [ "StandardsArn" ],
  "createOnlyProperties" : [ "/properties/StandardsArn" ],
  "readOnlyProperties" : [ "/properties/StandardsSubscriptionArn" ],
  "primaryIdentifier" : [ "/properties/StandardsSubscriptionArn" ],
  "additionalIdentifiers" : [ [ "/properties/StandardsArn" ] ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:GetEnabledStandards", "securityhub:BatchEnableStandards", "securityhub:UpdateStandardsControl" ]
    },
    "read" : {
      "permissions" : [ "securityhub:GetEnabledStandards", "securityhub:DescribeStandardsControls" ]
    },
    "update" : {
      "permissions" : [ "securityhub:GetEnabledStandards", "securityhub:UpdateStandardsControl" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:GetEnabledStandards", "securityhub:BatchDisableStandards" ]
    },
    "list" : {
      "permissions" : [ "securityhub:GetEnabledStandards" ]
    }
  }
}