import sys
import pkg_resources

package_dir = pkg_resources.resource_filename(__name__, "../src")
sys.path.append(package_dir)
