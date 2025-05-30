SCHEMA = {
  "typeName" : "AWS::Shield::Protection",
  "description" : "Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-shield.git",
  "primaryIdentifier" : [ "/properties/ProtectionArn" ],
  "readOnlyProperties" : [ "/properties/ProtectionId", "/properties/ProtectionArn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/ResourceArn" ],
  "replacementStrategy" : "delete_then_create",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False,
    "permissions" : [ "shield:ListTagsForResource", "shield:UntagResource", "shield:TagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "Name", "ResourceArn" ],
  "properties" : {
    "ProtectionId" : {
      "description" : "The unique identifier (ID) of the protection.",
      "type" : "string"
    },
    "ProtectionArn" : {
      "description" : "The ARN (Amazon Resource Name) of the protection.",
      "type" : "string"
    },
    "Name" : {
      "description" : "Friendly name for the Protection.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[ a-zA-Z0-9_\\.\\-]*"
    },
    "ResourceArn" : {
      "description" : "The ARN (Amazon Resource Name) of the resource to be protected.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "HealthCheckArns" : {
      "description" : "The Amazon Resource Names (ARNs) of the health check to associate with the protection.",
      "type" : "array",
      "insertionOrder" : False,
      "maxItems" : 1,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 2048
      }
    },
    "ApplicationLayerAutomaticResponseConfiguration" : {
      "$ref" : "#/definitions/ApplicationLayerAutomaticResponseConfiguration"
    },
    "Tags" : {
      "description" : "One or more tag key-value pairs for the Protection object.",
      "type" : "array",
      "insertionOrder" : False,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing or other management. Typically, the tag key represents a category, such as \"environment\", and the tag value represents a specific value within that category, such as \"test,\" \"development,\" or \"production\". Or you might set the tag key to \"customer\" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ],
      "properties" : {
        "Key" : {
          "description" : "Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as \"customer.\" Tag keys are case-sensitive.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as \"companyA\" or \"companyB.\" Tag values are case-sensitive.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      }
    },
    "ApplicationLayerAutomaticResponseConfiguration" : {
      "description" : "The automatic application layer DDoS mitigation settings for a Protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.",
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Action", "Status" ],
      "properties" : {
        "Action" : {
          "type" : "object",
          "description" : "Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.",
          "oneOf" : [ {
            "type" : "object",
            "additionalProperties" : False,
            "properties" : {
              "Count" : {
                "description" : "Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Count` action.\nYou must specify exactly one action, either `Block` or `Count`.",
                "type" : "object",
                "additionalProperties" : False
              }
            }
          }, {
            "type" : "object",
            "additionalProperties" : False,
            "properties" : {
              "Block" : {
                "description" : "Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Block` action.\nYou must specify exactly one action, either `Block` or `Count`.",
                "type" : "object",
                "additionalProperties" : False
              }
            }
          } ]
        },
        "Status" : {
          "description" : "Indicates whether automatic application layer DDoS mitigation is enabled for the protection.",
          "type" : "string",
          "enum" : [ "ENABLED", "DISABLED" ]
        }
      }
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "shield:CreateProtection", "shield:DeleteProtection", "shield:DescribeProtection", "shield:ListProtections", "shield:EnableApplicationLayerAutomaticResponse", "shield:AssociateHealthCheck", "shield:TagResource", "ec2:DescribeAddresses", "elasticloadbalancing:DescribeLoadBalancers", "route53:GetHealthCheck", "iam:GetRole", "iam:CreateServiceLinkedRole", "wafv2:GetWebACLForResource", "wafv2:GetWebACL" ]
    },
    "delete" : {
      "permissions" : [ "shield:DeleteProtection", "shield:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "shield:DescribeProtection", "shield:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "shield:DescribeProtection", "shield:AssociateHealthCheck", "shield:DisassociateHealthCheck", "shield:EnableApplicationLayerAutomaticResponse", "shield:UpdateApplicationLayerAutomaticResponse", "shield:DisableApplicationLayerAutomaticResponse", "shield:ListTagsForResource", "shield:TagResource", "shield:UntagResource", "route53:GetHealthCheck", "iam:GetRole", "iam:CreateServiceLinkedRole", "wafv2:GetWebACLForResource", "wafv2:GetWebACL" ]
    },
    "list" : {
      "permissions" : [ "shield:ListProtections" ]
    }
  }
}