/*
 * TypeDefs.hpp
 *
 *  Created on: March 18, 2014
 *      Author: Péter Fankhauser
 *	 Institute: ETH Zurich, Autonomous Systems Lab
 */

// Eigen
#include <Eigen/Core>

#pragma once

namespace grid_map {

  typedef Eigen::MatrixXf Matrix;
  typedef Eigen::Vector2d Position;
  typedef Eigen::Vector2d Vector;
  typedef Eigen::Vector3d Position3;
  typedef Eigen::Vector3d Vector3;
  typedef Eigen::Array2i Index;
  typedef Eigen::Array2i Size;
  typedef Eigen::Array2d Length;
  typedef uint64_t Time;

} /* namespace */
